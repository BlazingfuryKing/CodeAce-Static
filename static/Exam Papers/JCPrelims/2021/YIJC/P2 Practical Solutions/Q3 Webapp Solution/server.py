from flask import Flask, render_template, request
from sqlite3 import *

app=Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["POST"])   #[1]
def login():
    username = request.form.get('username')  #[1]get both username & password
    password = request.form.get('password')
    db = connect('shoppe.db')
    c = db.cursor()
    c.execute("SELECT id, name, email, pic FROM Account WHERE name=? AND password=?",(username,password))
    data = c.fetchone()        #[1] query
    db.close()

    if data == None:
        return index()      #[1] return to login page
    else:
        return render_template('display.html', data=data) #[1]


@app.route('/menu', methods=["POST"])
def menu():
    username = request.form.get('username')
    userid = request.form.get('userid')
    option = request.form.get('option')

    if option == 'update_profile':
        return render_template('profile.html', username=username, userid=userid)

    elif option == 'check_cart':
        db = connect('shoppe.db')
        c = db.cursor()
        c.execute("SELECT product_id, name,unit_price,quantity FROM Cart, Product WHERE Cart.product_id=Product.id AND Cart.customer_id=?", (userid,))
        data = c.fetchall()  #[1]
        db.close()
        return render_template('cart.html', data=data, username=username, userid=userid)
                            #[1] render page [1]username & id


@app.route('/update', methods=["POST"])
def update():
    f = request.files['mypic']  #[1]
    username = request.form.get('username')
    userid = request.form.get('userid')
    savefile='static/photo/'+username+'.png'#[1]
    f.save(savefile)#[1]

    msg = 'Profile picture uploaded successfully.'
    return render_template("success.html",display=msg) #[1]


@app.route('/checkout', methods=["POST"])
def checkout():
    username = request.form.get('username')
    userid = request.form.get('userid')
    select = request.form.getlist('select')   #[1]
    delivery_date = request.form.get('date')  #[1] for date and address
    delivery_address = request.form.get('address')
    
    if len(select) != 0:
        db = connect('shoppe.db')
        c = db.cursor()
        total = 0
        for productid in select:
            c.execute("SELECT quantity FROM Cart WHERE product_id=? AND customer_id=?", (productid,userid))
            qty = int(c.fetchone()[0]) 
            c.execute("SELECT unit_price FROM Product WHERE id=?", (productid,))
            price = float(c.fetchone()[0]) 
            c.execute('INSERT INTO Orders (customer_id,product_id,quantity,unit_price,delivery_date,delivery_address) VALUES (?,?,?,?,?,?)',(userid,productid,qty,price,delivery_date,delivery_address))
            db.commit()   #[2]insert into order table with 4 fields   #[1] date #[1] address
            total += qty*price #[1]
        total = "{:.2f}".format(round(total,2))
        db.close()
        
        msg = 'Checkout successfully. Total Cost: $' + total #[1]
        return render_template("success.html",display=msg)


app.run(debug=True, port=3500)
    

