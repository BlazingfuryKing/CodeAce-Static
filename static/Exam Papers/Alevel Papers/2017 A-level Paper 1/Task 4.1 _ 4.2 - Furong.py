'''
Task 4.1 & 4.2
'''

'''
Note:
Top down design is also known as a modular approach. Problems are usually
complex, which will require us to break them down into smaller, more
manageable problems to effectively and efficiently solve them.
'''

'''
Program Design
==============

class grid
    initialise: 4 rows (4 lists of 4 integers) as input
    methods: print grid

class row
    initialise: 4 integers as a list
    methods: print row

function call: print grid

'''

class row(object):
    def __init__(self, lst):
        self.lst = lst

    def printrow(self):
        return('{0:2}{1:2}{2:2}{3:2}'.format(self.lst[0],self.lst[1],
                                             self.lst[2],self.lst[3]))

class grid(object):
    def __init__(self, row1, row2, row3, row4):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4

    def printgrid(self):
        print(self.row1.printrow())
        print(self.row2.printrow())
        print(self.row3.printrow())
        print(self.row4.printrow())

#initialise grid
a = row([4,3,2,1])
b = row([1,2,4,3])
c = row([3,4,1,2])
d = row([2,1,3,4])

rows = grid(a,b,c,d)

rows.printgrid()    #prints the initial grid
