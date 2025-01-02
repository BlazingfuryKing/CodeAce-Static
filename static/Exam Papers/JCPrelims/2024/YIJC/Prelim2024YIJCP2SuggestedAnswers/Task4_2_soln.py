from flask import Flask, render_template, request
from sqlite3 import *
app = Flask(__name__)                                                   

@app.route('/')
def index():                                                            #[1m] default route and index function
    db = connect('LOYALTY.db')
    c = db.cursor()
    print('Connected')
    c.execute('''SELECT ConcertName, Artiste, Date, Price, Quantity \
        FROM Concert''')
    shows = c.fetchall()                                                #[1m] correct SELECT
    db.close()
    return render_template('index.html', shows = shows)                 #[1m] correct render

app.run(debug=False, port = 5000)

#index.html
#[1m] correct html format
#[1m] correct jinja code for displaying data (do not mark for table)
#[1m] run web app and save output file (regardless correct or wrong)