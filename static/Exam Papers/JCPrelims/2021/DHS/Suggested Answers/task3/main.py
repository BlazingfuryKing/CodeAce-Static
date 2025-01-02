from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import send_from_directory
from werkzeug.utils import secure_filename

import sqlite3
import os
import random
import datetime


db = sqlite3.connect('sanitisers.db')
db.execute('''DELETE FROM sanitisers''')

                
db.commit()
db.close()


file = open("sanitisers.txt")
list1 = []
for i in file:
    if i.replace('\n','').split(",")[0] != "product_name":
        list1.append((i.replace('\n','')).split(","))   
    

db = sqlite3.connect('sanitisers.db')
for i in list1:
    
    db.execute('''INSERT INTO sanitisers("product_name", "active_ingredient", "alcohol-based")
VALUES(?,?,?)''',(i[0],i[1],i[2]))

                
db.commit()
db.close()
file.close()



app = Flask(__name__) 


# Home page
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form['ingredient'])
        db = sqlite3.connect('sanitisers.db')
        cur = db.execute('''SELECT * FROM sanitisers WHERE active_ingredient="'''+ request.form['ingredient']+'''"''')
        display_list = []
        for i in cur:
            display_list.append(i)

        return render_template("display.html", display_list=display_list )

        
    db = sqlite3.connect('sanitisers.db')
    cur = db.execute('SELECT * FROM sanitisers')
    display_list = []
    for i in cur:
        display_list.append(i)

    return render_template("display.html", display_list=display_list )

app.run()

    

