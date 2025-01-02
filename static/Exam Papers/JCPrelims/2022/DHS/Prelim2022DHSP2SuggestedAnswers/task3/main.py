from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import sqlite3
import random


#if not os.path.isfile('ballot.db'): # Not required as sqlite3.connect covers this.
db = sqlite3.connect('ballot.db')
db.execute('''

CREATE TABLE IF NOT EXISTS `Names` (
	`nric`	TEXT,
	`names`	TEXT NOT NULL,
	PRIMARY KEY(`nric`)
);

''')


db.execute('''
CREATE TABLE IF NOT EXISTS `Results` (
	`nric`	TEXT,
	`group_id`	INTEGER,
	`ballot_result`	TEXT NOT NULL,
	FOREIGN KEY(`nric`) REFERENCES `Names`(`nric`),
	PRIMARY KEY(`nric`)
);


''')
db.execute("DELETE FROM Names ")
db.execute("DELETE FROM Results ")

db.execute('''

INSERT INTO `Names` VALUES ('T0663758C','Farah Yusoff'),
 ('S7829998G','Terry Sathyalingam'),
 ('T0487877S','Lin Wee Kiat Micheal'),
 ('S8735513R','Randal Khiatani'),
 ('T0254372E','Chen Chi Chien'),
 ('S9331280R','Natalie Lee'),
 ('S9981511E','Nayeli Sng Hui Hoon'),
 ('S7851994I','Cherilyn Leong'),
 ('S6450103G','Emma Wijeysingha');

''')

db.execute('''
INSERT INTO `Results` VALUES ('T0663758C',NULL,'yes'),
 ('S7829998G',4,'yes'),
 ('T0487877S',4,'no'),
 ('S8735513R',NULL,'yes'),
 ('T0254372E',NULL,'yes'),
 ('S9331280R',NULL,'no'),
 ('S9981511E',4,'yes'),
 ('S7851994I',6,'no'),
 ('S6450103G',6,'yes');

''')


db.commit()
db.close()
 

app = Flask(__name__) 


# Home page
@app.route("/")
def home():

    # Return value of randcss() is a random number which is assigned to the Jinja2
    # variable randcss. HTML file has a randcss Jinja2 placeholder concatenated at the end of the
    # linked .css stylesheet URL (for example "../style.css?q=523835382") to ensure
    # that the browser loads the latest stylesheet and not a cached stylesheet.
    return render_template('home.html', randcss=randcss())



# Dashboard page
@app.route("/dashboard/", methods=['GET', 'POST'])
def dashboard():
    
    # Check if there is POST data to process
    if 'nric_id' in request.form:
        
        # Check user credentials (access control)
        if correct_user(request.form['nric_id']):



            db = sqlite3.connect('ballot.db')
            cur = db.execute('''select ballot_result,group_id from Results where nric=?''',(request.form['nric_id'],))

            info = ""
            group = ""

            
            for row in cur:
                info = row[0]
            print(row)

            db.close()



            db = sqlite3.connect('ballot.db')
            cur = db.execute('''select names, ballot_result from Results, Names on Results.nric = Names.nric where (Results.group_id=(select group_id from Results where Results.nric=?) and Results.nric<>?)
''',(request.form['nric_id'],request.form['nric_id']))

            rows = []
            
            for row in cur:
                
                rowdetails=[]
                
                rowdetails.append(row[0])
                rowdetails.append(row[1])
             
                rows.append(rowdetails)

            db.close()

            if rows == []:
                rows = [["No group data", "No group data"]]


            return render_template('dashboard.html', 
            nric_id=request.form['nric_id'], rows=rows, info=info)
        
        return "Invalid NRIC."
    
    return redirect('/')



# Check user credentials (access control)
def correct_user(id_field):
    
    db = sqlite3.connect('ballot.db')
    db.row_factory = sqlite3.Row # convert cursor data to dictionary 
    
    cur = db.execute('SELECT * FROM Names')
    
    for row in cur:
        
        if row["nric"]==id_field:
            
            db.close()
            
            return True
        
    return False


# Generates number for appending to end of query for CSS to force browser
# to load the latest CSS stylesheet.
def randcss():
 
    return random.randint(1,99999)


if __name__ =="__main__":
    app.run()
