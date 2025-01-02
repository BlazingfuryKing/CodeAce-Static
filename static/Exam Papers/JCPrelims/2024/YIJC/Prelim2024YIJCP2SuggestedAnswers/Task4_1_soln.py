from sqlite3 import *
from flask import Flask, render_template, request
# app = Flask(__name__) 
db = connect('LOYALTY.db')
c = db.cursor()                                                             #[1m] connect and cursor

f = open('PURCHASE.txt')
next(f)
data = f.readlines()
for line in data:                           
    line = line.strip()
    ConcertID, Email, Quantity = line.split(',')                            #[1m] read, strip, split
    c.execute('''INSERT INTO Purchase(ConcertID, Email, Quantity) \
                VALUES(?,?,?)''', (ConcertID, Email, Quantity))
f.close()                                                                   #[1m] correct insert into Purchase

db.commit()                                                                 #[1m] commit and close db, close both files
db.close()

# app.run(debug=False, port = 5000)