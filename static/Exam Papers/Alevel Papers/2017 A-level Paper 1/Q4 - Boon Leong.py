example = [[4,3,2,1],[1,2,4,3],[3,4,1,2],[2,1,3,4]]

def display(sudoku):
    for line in sudoku:
        string = ''
        for char in line:
            string += str(char)
        print (string)

from random import randint

def trans1(sudoku):
    x = randint(0,1) #randomly choose which two rows to swap
    if x == 0:
        sudoku[0], sudoku[1] = sudoku[1], sudoku[0] #swap top two rows
    else:
        sudoku[2], sudoku[3] = sudoku[3], sudoku[2] #swap bottom two rows
    return sudoku

def trans2(sudoku):
    x = randint(0,1) #randomly choose which two columns to swap
    if x == 0:
        for i in range(4):
            sudoku[i][0], sudoku[i][1] = sudoku[i][1], sudoku[i][0] #swap left two columns
    else:
        for i in range(4):
            sudoku[i][2], sudoku[i][3] = sudoku[i][2], sudoku[i][3] #swap right two columns
    return sudoku

def trans3(sudoku):
    sudoku[0], sudoku[1], sudoku[2], sudoku[3] = sudoku[2], sudoku[3], sudoku[0], sudoku[1] #swaps rows (1 and 2) with (3 and 4)
    return sudoku

def trans4(sudoku):
    for i in range(4):
        sudoku[i][0], sudoku[i][1], sudoku[i][2], sudoku[i][3] = sudoku[i][2], sudoku[i][3], sudoku[i][1], sudoku[i][0] #swaps columns (1 and 2) with (3 and 4)
    return sudoku

def createnew(sudoku, x):
    if x == 0:
        newsudoku=trans1(sudoku)
    if x == 1:
        newsudoku=trans2(sudoku)
    if x == 2:
        newsudoku=trans3(sudoku)
    if x == 3:
        newsudoku=trans4(sudoku)
    return(newsudoku)

display(example)

x = randint(0, 3)
if x == 0:
    print('Transformation 1: Swaps two rows in the same quadrant')
if x == 1:
    print('Transformation 2: Swaps two columns in the same quadrant')
if x == 2:
    print('Transformation 3: Swaps the top and bottom quadrant rows entirely')
if x == 3:
    print('Transformation 4: Swaps the left and right quadrant columns entirely')
sudo1 = createnew(example, x)
display(sudo1)

y = randint(0, 3)
if y == 0:
    print('Transformation 1: Swaps two rows in the same quadrant')
if y == 1:
    print('Transformation 2: Swaps two columns in the same quadrant')
if y == 2:
    print('Transformation 3: Swaps the top and bottom quadrant rows entirely')
if y == 3:
    print('Transformation 4: Swaps the left and right quadrant columns entirely')
sudo2 = createnew(sudo1, x)
display(sudo2)

