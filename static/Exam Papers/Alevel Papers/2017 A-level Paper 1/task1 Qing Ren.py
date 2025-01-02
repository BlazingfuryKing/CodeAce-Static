#Task 1.1
file1 = open('INVENTORY.txt')
Inventory = file1.read().splitlines() #read until end of file and split the line up
ItemTypes = set(Inventory)
ItemCounts = {}
for item in Inventory:
    if item in ItemCounts:
        ItemCounts[item] += 1
    else:
        ItemCounts[item] = 1
print("ItemType" + 10*" " + "Count")
for item in ItemCounts:
    n = 18 - len(str(item))
    print(item + n*" " + str(ItemCounts[item]))