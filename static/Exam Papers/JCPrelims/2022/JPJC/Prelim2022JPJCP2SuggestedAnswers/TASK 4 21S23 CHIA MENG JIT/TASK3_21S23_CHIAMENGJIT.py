import pymongo, json

#creation of database
client = pymongo.MongoClient("127.0.0.1", 27017)
lst_database = client.database_names()
if "StyleTheory" in lst_database:#if database already exists
    client.drop_database("StyleTheory")
db = client.get_database("StyleTheory")
coll = db.get_collection("Rental")

#opening json file to insert into database
file = open("RENTAL.JSON", 'r')
lst_data = json.load(file)
file.close()

coll.insert_many(lst_data)
print("Inserted items")
client.close()


#task 3.2
def ui():
    #will display user interface and return the user's input
    print("\nStyle Theory\nOption 1 - Insert new rental\nOption 2 - Update existing rental\nOption 3 - Quit")
    data = input("Enter your option ( 1, 2, or 3): ")
    while data.isnumeric() != True:
        print("\nPlease enter a valid field")
        data = input("Enter your option ( 1, 2, or 3): ")
        
    return int(data)

def get_fields():
    cataloguenumber = int(input("Catalogue number"))
    brand = input("Brand")
    category = input("category? (Apparel or Bag)")
    rental = int(input("daily rental fee"))
    email = input("email")
    start_date = input("start date")
    end_date = input("end date")
    if category == "Apparel":
        size = int(input("size"))
        return {"catalogueNumber": cataloguenumber,
                "brand": brand, "category": category,
                "rental":rental, "size":size, "email":email,
                "startDate": start_date, "endDate": end_date}
    return {"catalogueNumber": cataloguenumber,
                "brand": brand, "category": category,
                "rental":rental, "email":email,
                "startDate": start_date, "endDate": end_date}
    
def main_input():
    #to handle input request from user
    while True: 
        data = ui()
        if data == 3: #quit condition
            return #break out of the loop
        client = pymongo.MongoClient("127.0.0.1", 27017)
        db = client.get_database("StyleTheory")
        coll = db.get_collection("Rental")
        if data == 1: # insert condition
            #goal is to get all the relevant fields
            print('\ninsert data\n')
            user_data = get_fields()
            coll.insert_one(user_data)
            print("inserted")

        if data == 2:
            print('\nupdate data\n')
            cataloguenumber = input("catalogue number")
            start_date = input("start date")
            end_date = input("new end date")
            query = {"catalogueNumber":cataloguenumber, "startDate": start_date}
            coll.update_one(query, {"$set":{"endDate":end_date}} )
            print("updated")
        client.close()
            

#=====main program for task 3.2========
main_input()

#task 3.3
from datetime import date
def display_all():
    client = pymongo.MongoClient("127.0.0.1", 27017)
    db = client.get_database("StyleTheory")
    coll = db.get_collection("Rental")
    cur = coll.find() #returns all documents in collection
    print("{0:20}{1:15}{2:15}{3:20}{4:10}{5:30}{6:13}{7:13}{8:13}".format("Catalogue Number", "Brand", "Category", "Daily Rental Fee",
                    "Size", "Customer Email", "Start Date", "End Date",
                    "Total Amount Payable")
          )
    for doc in cur:
        #finding the date difference
        f_day = doc["startDate"].split('-')
        f_date = date(int(f_day[0]),int(f_day[1]),int(f_day[2]))
        l_day = doc["endDate"].split('-')
        l_date = date(int(l_day[0]),int(l_day[1]),int(l_day[2]))
        delta = l_date - f_date
        days = delta.days

        #assigning all required attributes to print
        size = "NA"
        cataloguenumber, brand, category, rental, email, start_date, end_date = doc["catalogueNumber"],doc['brand'], doc['category'], doc['rental'], doc['email'], doc['startDate'], doc['endDate']
        if 'size' in doc:
            size = str(doc['size'])
        total_payable = days * (rental) #calculation of total am
        print("{0:20}{1:15}{2:15}{3:20}{4:10}{5:30}{6:13}{7:13}{8:13}".format(
            str(cataloguenumber), brand, category, str(rental), size, email, start_date, end_date, str(total_payable))
              )
        
    client.close()

