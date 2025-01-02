'''
Task 4.3
'''
from random import *

#creates a row in the grid
class row(object):
    def __init__(self, lst):
        self.lst = lst

    def printrow(self):
        return('{0:2}{1:2}{2:2}{3:2}'.format(self.lst[0],self.lst[1],
                                             self.lst[2],self.lst[3]))
    
#creates a grid with 4 methods of transformation
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

    def transform1(self):
        choice = randint(1,2)   #generates a random number to decide
                                #which pair of rows to swap
        #print(choice)          #prints the random value generated
        if choice == 1: #swap row 1 with row 2
            self.row1, self.row2 = self.row2, self.row1
        else:           #swap row 3 with row 4
            self.row3, self.row4 = self.row4, self.row3
        print("Tranformation 1: Swaps two rows in the same quadrants")
        return self.printgrid()

    def transform2(self):
        choice = randint(1,2)   #generates a random number to decide
                                #which pair of rows to swap
        #print(choice)          #prints the random value generated
        if choice == 1: #swap column 1 with column 2
            self.row1.lst[0], self.row1.lst[1] = self.row1.lst[1], self.row1.lst[0]
            self.row2.lst[0], self.row2.lst[1] = self.row2.lst[1], self.row2.lst[0]
            self.row3.lst[0], self.row3.lst[1] = self.row3.lst[1], self.row3.lst[0]
            self.row4.lst[0], self.row4.lst[1] = self.row4.lst[1], self.row4.lst[0]
        else:           #swap column 3 with column 4
            self.row1.lst[2], self.row1.lst[3] = self.row1.lst[3], self.row1.lst[2]
            self.row2.lst[2], self.row2.lst[3] = self.row2.lst[3], self.row2.lst[2]
            self.row3.lst[2], self.row3.lst[3] = self.row3.lst[3], self.row3.lst[2]
            self.row4.lst[3], self.row4.lst[3] = self.row4.lst[3], self.row4.lst[2]
        print("Transformation 2: Swaps two columns in the same quadrants")
        return self.printgrid()            

    def transform3(self):
        print("Transformation 3: Swaps the top and bottom quadrant rows entirely") 
        self.row1, self.row2, self.row3, self.row4 = self.row3, self.row4, self.row1, self.row2
        return self.printgrid()

    def transform4(self):
        print("Transformation 4: Swaps the left and right quadrant columns entirely")
        self.row1.lst[0], self.row1.lst[1], self.row1.lst[2], self.row1.lst[3] = self.row1.lst[2], self.row1.lst[3], self.row1.lst[0], self.row1.lst[1]
        self.row2.lst[0], self.row2.lst[1], self.row2.lst[2], self.row2.lst[3] = self.row2.lst[2], self.row2.lst[3], self.row2.lst[0], self.row2.lst[1]
        self.row3.lst[0], self.row3.lst[1], self.row3.lst[2], self.row3.lst[3] = self.row3.lst[2], self.row3.lst[3], self.row3.lst[0], self.row3.lst[1]
        self.row4.lst[0], self.row4.lst[1], self.row4.lst[2], self.row4.lst[3] = self.row4.lst[2], self.row4.lst[3], self.row4.lst[0], self.row4.lst[1]
        return self.printgrid()
        

#initialise grid
a = row([4,3,2,1])
b = row([1,2,4,3])
c = row([3,4,1,2])
d = row([2,1,3,4])

rows = grid(a,b,c,d)

rows.printgrid()    #prints the initial grid
print('')
#rows.transform1()   #prints the grid after transformation 1
#rows.transform2()
#rows.transform3()
#rows.transform4()
