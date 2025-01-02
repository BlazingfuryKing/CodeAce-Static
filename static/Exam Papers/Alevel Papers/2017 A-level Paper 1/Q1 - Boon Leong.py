file = open("INVENTORY.txt", "r") 
Inventory = file.readlines()
for x in range(len(Inventory)):
    if Inventory[x][-1:]=='\n':
        new = Inventory[x][:-1]
        Inventory[x]=new
        

ItemTypes = []
for item in Inventory:
    if item not in ItemTypes:
        ItemTypes.append(item)

ItemCounts = []
for item in ItemTypes:
    count = Inventory.count(item)
    ItemCounts.append(count)

maxlength = 0
for item in ItemTypes:
    if len(item) > maxlength:
        maxlength = len(item)
maxlength = max(8, maxlength)

print('ItemType'+(maxlength - 7)*' '+'Count')
for x in range(len(ItemTypes)):
    print(ItemTypes[x] + (maxlength - len(ItemTypes[x])+1)*' ' + str(ItemCounts[x]))
