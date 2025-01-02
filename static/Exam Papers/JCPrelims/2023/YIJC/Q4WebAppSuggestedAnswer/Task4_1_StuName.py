from sqlite3 import *

db = connect('Taxi.db')
c = db.cursor()

c.execute('''DROP TABLE IF EXISTS Feedback''')

c.execute('''CREATE TABLE Feedback (
     ID INTEGER PRIMARY KEY AUTOINCREMENT,
     DriverID INTEGER NOT NULL REFERENCES Driver(ID),
     Date TEXT NOT NULL,
     Feedback TEXT)''')
                                    # [1m] create table with 4 fields

                                    # [1m] DriverID as foreign key

f = open('Feedback.TXT')            # [1m] open and close text file
lines = f.readlines()
        
for line in lines[1:]:              # [1m] skip header, iterate thru lines 
    line = line.strip().split(',')  # [1m] strip and split
    c.execute('''INSERT INTO Feedback 
        (DriverID, Date, Feedback) 
        VALUES (?,?,?)''', line)    # [1m] insert data into table
f.close()

db.commit()
db.close()
