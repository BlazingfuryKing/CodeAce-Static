#------Read & Set up Data strutures------#

#open inventory.txt
inv_open = open('inventory.txt','r')

#read all lines into a list
inv_read = inv_open.readlines()

#strip '\n' from list item
#Bullet Point No.1
inventory = []
for i in inv_read:
    inventory += [i.strip()]

#ItemTypes - list of all types of items (no duplicates)
#Bullet Point No.2
ItemTypes = []

for i in inventory:
    while i not in ItemTypes:
        ItemTypes += [i]

#print(ItemTypes)

#ItemCounts
#Bullet Point No.3
ItemCounts = []

for i in ItemTypes:
    count = 0
    for j in inventory:
        if j == i:
            count += 1
    ItemCounts += [count]    

#print(ItemCounts)

#------Print Input File------#
#Bullet Point No.4(i)
print('Input File:')
for i in ItemTypes:
    print(i.strip()) #removes '\n'

print('\n')

#------Create Output file------#
#Bullet Point No.4(ii)
output = [['ItemType', 'Count'],['','']]

#alignment calculation
max_length = 0
for i in ItemTypes:
    max_length = max(max_length,len(i))

#output rows    
for i in range(len(ItemCounts)):
    output += [[ItemTypes[i], ItemCounts[i]]]

#print output
for row in output:
    print(row[0],' '*(max_length+2-len(row[0])),row[1]) #additional 2 spaces

