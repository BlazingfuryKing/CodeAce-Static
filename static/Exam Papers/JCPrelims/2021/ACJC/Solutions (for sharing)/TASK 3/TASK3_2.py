# TASK 3.2 [7m]
import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)
db = client.get_database("community_centre")
coll = db.get_collection("management_committee") # [1] Set up client and close later

if coll.find().count != 0:
    coll.delete_many({}) # [1] Clear the collection if it already exists

with open("VACCINATION.txt") as f1:
    for line in f1:
        lst = line.strip().split(",") # [1] Open file and process each line
        
        mem_id, name = int(lst[0]), lst[1] # [1] Handle member ID and name
        first, second = "N/A", "N/A"
        remarks = None

        # [1] Handle remarks
        if not lst[-1].isnumeric() and len(lst) > 2:
            remarks = lst[-1]
            lst.pop()

        # [1] Handle date of first and second dose
        if len(lst) == 3:
            first = lst[2]
        elif len(lst) == 4:
            first = lst[2]
            second = lst[3]

        # [1] Insert documents
        if remarks:
            coll.insert_one({"_id":mem_id,
                             "name":name,
                             "date_first_dose":first,
                             "date_second_dose":second,
                             "remarks":remarks}) 
        else:
            coll.insert_one({"_id":mem_id,
                             "name":name,
                             "date_first_dose":first,
                             "date_second_dose":second})

client.close()
