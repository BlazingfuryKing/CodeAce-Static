from flask import Flask, render_template, request
from sqlite3 import *
app = Flask(__name__)

@app.route('/')
def index():
    db = connect('LOYALTY.db')
    c = db.cursor()
    print('Connected')
    c.execute('''SELECT ConcertName, Artiste, Date, Price, Quantity \
        FROM Concert''')
    shows = c.fetchall()
    db.close()
    return render_template('index.html', shows = shows)

@app.route('/booking')
def booking():                                                  
    db = connect('LOYALTY.db')
    c = db.cursor()
    print('Connected')
    c.execute('SELECT ConcertID, ConcertName FROM Concert')
    shows = c.fetchall()                                        
    db.close()
    return render_template('booking.html', shows = shows)        

@app.route('/check', methods = ['POST'])                                    #[1m] app route matches form route, POST included
def check():
    email = request.form.get('email')
    pw = request.form.get('pw')
    concert_id = request.form.get('concert')
    qty = request.form.get('qty')                                           #[1m] request for form input
    
    db = connect('LOYALTY.db')
    c = db.cursor()
    
    c.execute('''SELECT MemberName from Member WHERE Email = ? \
        AND Password = ?''', (email, pw))                                   #[1m] email + pw check
    user = c.fetchone()
    if not user:
        return 'Invalid account.'
        db.close()                                                          #[1m] render invalid acct return
    else:
        c.execute('''INSERT INTO Purchase(ConcertID, Email, Quantity) \
            VALUES(?,?,?)''', (concert_id, email, int(qty)))

        c.execute('''UPDATE Concert SET Quantity = Quantity - ? \
            WHERE ConcertID = ?''', (int(qty), concert_id))                 #[1m] update Purchase or Concert table
        
        c.execute('''SELECT ConcertName, Artiste, Date, Price \
            FROM Concert WHERE ConcertID = ?''', (concert_id,))              
        
        data = c.fetchone()                                                 #[1m] retrieve concert details from db
        total_amt = int(data[3]) * int(qty)                                 #[1m] calc total amt
        package = list(data) + [qty, total_amt, user[0], email]
        
        db.commit()
        db.close()
        return render_template('success.html', package = package)           #[1m] render to success.html + package
        
app.run(debug=False, port = 5000)



#success.html
#[1m] Correct display