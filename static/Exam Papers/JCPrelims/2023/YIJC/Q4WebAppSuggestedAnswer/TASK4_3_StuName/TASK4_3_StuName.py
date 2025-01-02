from flask import *

app = Flask(__name__)                               


@app.route('/')                           
def index():                              
    return render_template('index.html')  
                                          

from sqlite3 import *

@app.route('/check', methods = ['POST'])      #1m /check route with POST method
def check():
    driverID = request.form.get('DriverID')   #1m get DriverID
    db = connect('Taxi.db')
    c = db.cursor()
    c.execute("""SELECT Name from Driver where ID = ?""", (driverID,))
    name = c.fetchone()                     #1m query for driver's name

    if name == None:
        db.close()
        print('Driver ID not found.')
    else:                                   
        c.execute("""SELECT * from Vehicle""")  #1m query all the vehicle info
        data = c.fetchall()
        db.close()

        taxis = []
        i = 1
        for vehicle in data:             #1m create a list of vehicle info 
            taxis.append([i,vehicle[0],vehicle[1],vehicle[3]]) 
            i = i+1
            
        return render_template('rental.html', driverID=driverID,
                                   name=name[0], taxis=taxis)
                                #1m render rental.html with all necessary data

app.run(debug = False, port = 5000)   
