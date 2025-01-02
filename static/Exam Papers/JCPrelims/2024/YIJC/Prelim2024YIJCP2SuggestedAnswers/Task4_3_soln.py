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
def booking():                                                  #[1m] correct booking route
    db = connect('LOYALTY.db')
    c = db.cursor()
    print('Connected')
    c.execute('SELECT ConcertID, ConcertName FROM Concert')
    shows = c.fetchall()                                        #[1m] correct select and fetchall
    db.close()
    return render_template('booking.html', shows = shows)       #[1m] correct render 


app.run(debug=False, port = 5000)

#booking.html
#[1m] correct form action and POST
#[1m] correct text form items (email, password, qty) [allow 1 slip]
#[1m] correct jinja for show list (accept dropdown or radio) + use ConcertID as reference

