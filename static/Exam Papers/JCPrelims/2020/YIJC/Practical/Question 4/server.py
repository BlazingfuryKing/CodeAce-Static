from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkin', methods=['POST'])
def checkin():
    if request.method == 'POST':
        db = sqlite3.connect('covid.db')
        c = db.cursor()

        PostalCode = request.form.get('postal_code')
        Date = request.form.get('date')
        CheckIn = request.form.get('check_in_time')
        NRIC = request.form.get('nric')
        Phone = request.form.get('phone')

        info = [NRIC, Phone, PostalCode, CheckIn, Date]

        if '' in info:
            warning = 'Please fill up all of the required information'
            return render_template('index.html', warning=warning)

        CheckOut = ''
        info = [NRIC, Phone, PostalCode, CheckIn, CheckOut, Date]
        
        c.execute('''INSERT INTO event (NRIC, Phone, PostalCode, CheckIn, CheckOut, Date)
                    VALUES (?, ?, ?, ?, ?, ?)''', info)
        
        db.commit()
        db.close()

        return render_template('checkout.html')



@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if request.method == 'GET':
        return render_template('checkout.html')

    else:

        PostalCode = request.form.get('postal_code')
        Date = request.form.get('date')
        CheckOut = request.form.get('check_out_time')
        NRIC = request.form.get('nric')
        Phone = request.form.get('phone')

        info = [PostalCode, Date, NRIC, Phone]

        if '' in info or CheckOut=='':
            warning = 'Please fill up all of the required information.'
            return render_template('checkout.html', warning=warning)

        else:

            db = sqlite3.connect('covid.db')
            c = db.cursor()
    
            c.execute('''SELECT CheckOut FROM event
                        WHERE PostalCode = ? AND Date = ? AND
                        NRIC = ? AND Phone = ?''', info)
            data = c.fetchall()

            if len(data) == 0:
                warning = 'Please enter valid information.'
                db.close()
                return render_template('checkout.html', warning=warning)      

            elif data[0][0]=='':
                info = [CheckOut, PostalCode, Date, NRIC, Phone]
                c.execute('''UPDATE event SET CheckOut = ?
                            WHERE PostalCode = ? AND Date = ? AND
                            NRIC = ? AND Phone = ? AND CheckOut = ""
                            ''', info)
                db.commit()
                db.close()
                return render_template('finish.html')
            
            else:
                warning = 'Record has been previously Checked Out.'
                db.close()
                return render_template('checkout.html', warning=warning)      


app.run(debug=True, port=5002)


