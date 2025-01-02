import sqlite3

conn = sqlite3.connect("JPFashion.db")

#customer
customer_file = open("CUSTOMER.TXT",'r')
customer_file.readline() #header
for line in customer_file:
    Email,FirstName,LastName,ContactNumber,DOB,Address = line.strip().split(",")
    conn.execute("insert into Customer values (?,?,?,?,?,?)",(Email,FirstName,LastName,ContactNumber,DOB,Address))
    conn.commit()
customer_file.close()



#product
product_file = open("PRODUCT.TXT",'r')
product_file.readline()
for line in product_file:
    CatalogueNumber,Category,Brand,Size,Fee = line.strip().split(",")
    CatalogueNumber = int(CatalogueNumber)
    Size = int(Size)
    Fee = int(Fee)
    conn.execute("insert into Product values (?,?,?,?,?)",(CatalogueNumber,Category,Brand,Size,Fee))
    conn.commit()
product_file.close()


#customer rental
customer_rental_file = open("CUSTOMERRENTAL.TXT",'r')
customer_rental_file.readline()
for line in customer_rental_file:
    ID,Email,StartDate,EndDate = line.strip().split(",")
    ID = int(ID)
    conn.execute("insert into CustomerRental values (?,?,?,?)",(ID,Email,StartDate,EndDate))
    conn.commit()
customer_rental_file.close()

#product rental
product_rental_file = open("PRODUCTRENTAL.TXT",'r')
product_rental_file.readline()
for line in product_rental_file:
    ID,CatalogueNumber,Returned = line.strip().split(",")
    ID = int(ID)
    CatalogueNumber = int(CatalogueNumber)
    if Returned == "TRUE":
        Returned = 1
    else:
        Returned = 0
    conn.execute("insert into ProductRental values (?,?,?)",(ID,CatalogueNumber,Returned))
    conn.commit()

product_rental_file.close()

conn.close()
