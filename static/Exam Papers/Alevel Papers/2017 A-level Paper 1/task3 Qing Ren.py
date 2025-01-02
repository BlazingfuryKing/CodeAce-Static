class ConnectionNode(object):
    def __init__(self, value = None, left = None, right = None):
        self.DataValue = value
        self.LeftChild = 0
        self.RightChild = 0

RobotData = []
for i in range(26):
    RobotData += [ConnectionNode()]
    if i >0:
        RobotData[i-1].LeftChild = i
Root = 1
NextFreeChild = 1
        
def FindNode(NodeValue):
    global Root
    Found = False
    CurrentPosition = Root
    while Found == False and CurrentPosition <= 25:
        if RobotData[CurrentPosition].DataValue == NodeValue:
            Found = True
        else:
            CurrentPosition += 1
    if CurrentPosition > 25:
        return 0
    else:
        return CurrentPosition
    
def AddToRobotData(NewDataItem, ParentItem, ThisMove):
    global Root
    global NextFreeChild
    if Root == 1 and NextFreeChild == 1:
        NextFreeChild = RobotData[NextFreeChild].LeftChild
        RobotData[Root].LeftChild = 0
        RobotData[Root].DataValue = NewDataItem
    else:
        ParentPosition = FindNode(ParentItem)
        if ParentPosition > 0:
            ExistingChild = FindNode(NewDataItem)
            if ExistingChild > 0:
                ChildPointer = ExistingChild
            else:
                ChildPointer = NextFreeChild
                NextFreeChild = RobotData[NextFreeChild].LeftChild
                RobotData[ChildPointer].LeftChild = 0
                RobotData[ChildPointer].DataValue = NewDataItem
            if ThisMove == 'L':
                RobotData[ParentPosition].LeftChild = ChildPointer
            else:
                RobotData[ParentPosition].RightChild = ChildPointer

def OutputData():
    print(Root)
    print(NextFreeChild)
    for i in range(1,len(RobotData)):
        print('DataValue:', RobotData[i].DataValue)
        print('LeftChild:', RobotData[i].LeftChild)
        print('RightChild:', RobotData[i].RightChild)

f1 = open('SEARCHTREE.txt', 'r')
data = f1.read().splitlines()
data2 = map(lambda x: x.split(','), data)
for item in data2:
    AddToRobotData(item[0], item[1], item[2])
    
                
OutputData()
        
def tree_traverse(node, previous = ''):
    new = previous + node.DataValue
    if node.DataValue == 'Z':
        print(new)
        return None
    elif node.LeftChild == 0 and node.RightChild == 0:
        return None
    #print(node.DataValue)
    if node.LeftChild != 0:
        tree_traverse(RobotData[node.LeftChild], new)
        #start = node.DataValue   
    if node.RightChild != 0:
        #print('restart at:', start)
        tree_traverse(RobotData[node.RightChild], new)



print(tree_traverse(RobotData[1]))
