from flask import *

app = Flask(__name__)                               


@app.route('/')                           
def index():                              
    return render_template('index.html')
 

from sqlite3 import *

@app.route('/check', methods = ['POST'])
def check():
    driverID = request.form.get('DriverID')
    db = connect('Taxi.db')  
    c = db.cursor()
    c.execute("""SELECT Name from Driver where ID = ?""", (driverID,))
    name = c.fetchone()
                                               
    if name == None:
        db.close()
        print('Driver ID not found.')
    else:                                   
        c.execute("""SELECT * from Vehicle""")  
        data = c.fetchall()
        db.close()

        taxis = []
        i = 1
        for vehicle in data:
            taxis.append([i,vehicle[0],vehicle[1],vehicle[3]]) 
            i = i+1
                                           
        return render_template('rental.html', driverID=driverID,
                                   name=name[0], taxis=taxis)

@app.route('/rental', methods=['POST'])      
def rental():
    driverid = request.form.get('driverid')
    date = request.form.get('date')
    vehicle = request.form.get('license')
    db = connect('Taxi.db')
    c = db.cursor()
                                            
    c.execute('''SELECT * FROM Rent
                 where License = ? AND date = ?;''',(vehicle,date))
    result = c.fetchone()                    
    
    if result != None:
        db.close()
        return render_template('message.html',message='Vehicle unavailable for the selected date.')
    else:
        c.execute('''INSERT INTO Rent Values (?,?,?,"No")''',(driverid,vehicle,date))
        db.commit()                          
#Task 4.5 (7m) #############################################################################
        c.execute('''SELECT Date,Model,Cost,Paid FROM Rent, Vehicle WHERE
                        Vehicle.License = Rent.License AND DriverID = ?''',(driverid,))
        results = c.fetchall()             # 1m query all the rental records for this driverid         

        c.execute('''SELECT SUM(Cost) FROM Rent, Vehicle WHERE
                        Vehicle.License = Rent.License AND
                        Paid = 'No' AND DriverID = ?''',(driverid,))
        total = c.fetchone()               # 1m compute the total cost
        
        total = "${:.2f}".format(total[0]) # 1m for $ and 2dp formatting
        db.close()                  

                                            
        db.close()                         # 1m render success.html with info
        return render_template('success.html',message='Rental Successful',
                                           results = results,total=total)
                                           # (3m in success.html)

app.run(debug = False, port = 5000)   
   

