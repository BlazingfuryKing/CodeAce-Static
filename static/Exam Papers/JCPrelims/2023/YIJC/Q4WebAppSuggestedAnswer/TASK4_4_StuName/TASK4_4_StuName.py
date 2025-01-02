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

@app.route('/rental', methods=['POST'])     # 1m /rental route with POST method
def rental():
    driverid = request.form.get('driverid') # 1m get Driver ID, date, license
    date = request.form.get('date')
    vehicle = request.form.get('license')
    db = connect('Taxi.db')
    c = db.cursor()
                                            
    c.execute('''SELECT * FROM Rent
                 where License = ? AND date = ?;''',(vehicle,date))
    result = c.fetchone()               # 1m query check for vehicle availability
    
    if result == None:
        c.execute('''INSERT INTO Rent VALUES (?,?,?,"No")''',(driverid,vehicle,date))
                                # 1m Insert record into Rent tabel with 'No' for Paid
        db.commit()                         
        db.close()
        return render_template('message.html',message='Rental Successful.')
    else:
        db.close()                          # 1m render html or return appropriate message
        return render_template('message.html',message='Vehicle unavailable for the selected date.')
                                                    
app.run(debug = False, port = 5000)   
   

