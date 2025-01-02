#open, read and create new list
isbn_open = open('ISBNPRE.txt','r')

isbn_read = isbn_open.readlines()

isbn_lst = []
for i in isbn_read:
    isbn_lst += [i.strip()]


#CalCheckDigit program#
def CalCheckDigit(Number, Total):
    #print('length number',len(Number))
    if len(Number) > 1:
        Digit = int(Number[0])
        Total += Digit * (len(Number)+1)
        NewNumber = Number[1:]
        #print('NewNumber',NewNumber)
        CheckDigit = CalCheckDigit(NewNumber, Total)    #A

    else:
        Digit = int(Number)
        Total += Digit * (len(Number)+1)
        #print('Total',Total)
        CalcModulus = Total%11
        #print('Mod',CalcModulus)
        CheckValue = 11 - CalcModulus
        #print('CheckValue',CheckValue)

        if CheckValue == 11:
            return '0'
        elif CheckValue == 10:
            return 'X'      #B
        else:
            return CheckValue

    if len(Number) == 9:
        return Number+str(CheckDigit)    #C
    else:
        return CheckDigit


#Calculate result for each entry in ISBNPRE.TXT and print on screen

for i in isbn_lst:
    print('File Entry:',i,"   ISBN:",CalCheckDigit(i,0))

