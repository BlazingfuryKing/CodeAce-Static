import sqlite3

#creating database
db = sqlite3.connect("JPFashion.db")
sql = open("TASK4_1_21S23_CHIAMENGJIT.sql", 'r')
command = ''
for line in sql:
    command += line
    if ';' in command:
        db.execute(command)
        db.commit()
        command = ''
print("Created database")

#opening all text files
customer = open("CUSTOMER.TXT", 'r')
product = open("PRODUCT.TXT", 'r')
customer_rental = open("CUSTOMERRENTAL.TXT", 'r')
product_rental = open("PRODUCTRENTAL.TXT", 'r')


#reading CUSTOMER.TXT
customer.readline()
for line in customer:
    email, firstname, lastname, contact, dob, address = line.strip().split(',')
    db.execute('''
            INSERT INTO Customer(Email, FirstName, LastName, ContactNumber, DOB,
            Address) VALUES(?, ?, ?, ?, ?, ?)
            ''', (email, firstname, lastname, contact, dob, address)
               )
    db.commit()

#reading PRODUCT.TXT
product.readline()
for line in product:
    cataloguenumber, category, brand, size, fee = line.strip().split(',')
    db.execute('''
            INSERT INTO Product(CatalogueNumber, Category, Brand, Size, Fee)
            VALUES(?, ?, ?, ?, ?)
            ''', (cataloguenumber, category, brand, size, fee)
               )
    db.commit()

#reading CUSTOMERRENTAL.TXT
customer_rental.readline()
for line in customer_rental:
    ID, email, startdate, enddate = line.strip().split(',')
    db.execute('''
            INSERT INTO CustomerRental(ID, Email, StartDate, EndDate)
            VALUES(?,?,?,?)
            ''', (ID, email, startdate, enddate)
               )
    db.commit()

#reading PRODUCTRENTAL.TXT
product_rental.readline()
for line in product_rental:
    ID, cataloguenumber, returned = line.strip().split(',')
    db.execute('''
            INSERT INTO ProductRental(ID, CatalogueNumber, Returned)
            VALUES(?,?,?)
            ''', (ID, cataloguenumber, returned)
                )
    db.commit()

print("Inserted all records")
#closing all files
customer.close()
product.close()
customer_rental.close()
product_rental.close()
sql.close()
db.close()
