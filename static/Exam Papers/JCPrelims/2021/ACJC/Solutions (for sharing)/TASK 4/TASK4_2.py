import sqlite3

# connect to the SQL database, commit and close it later
connection = sqlite3.connect("bento_company.db")

kiosk_lst = []
bento_lst = []
markup = [2.60, 2.90, 2.40, 3.10]

# open and process each line in the text file
# insert records into Kiosk table 
with open("KIOSK.txt") as f1:
    for line in f1:
        lst = line.strip().split(",")
        kiosk_lst.append(int(lst[0])) # extract only the KioskID to kiosk_lst
        connection.execute("INSERT INTO Kiosk VALUES (?, ?, ?)",
                           (int(lst[0]), lst[1], float(lst[2])))

# insert records into BentoBox table
with open("BENTOBOX.txt") as f2:
    for line in f2:
        lst = line.strip().split(",")
        bento_lst.append([lst[0], float(lst[1])]) # extract only the bento name and price to bento_lst
        connection.execute("INSERT INTO BentoBox VALUES (?, ?, ?, ?, ?)",
                           (lst[0], float(lst[1]), int(lst[2]), int(lst[3]), int(lst[4])))

# [1] insert 4x8 records into KioskBento table
for i in range(len(kiosk_lst)):
    kiosk = kiosk_lst[i]
    for j in range(len(bento_lst)):
        bento = bento_lst[j][0]
        price = float(bento_lst[j][1]) + markup[i] # [1] add markup price
        connection.execute("INSERT INTO KioskBento VALUES (?, ?, ?)",
                           (kiosk, bento, price))

connection.commit()
connection.close()
