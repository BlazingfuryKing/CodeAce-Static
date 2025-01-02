##A: CalCheckDigit(NewNumber, Total)
##B: RETURN STRING(X)
##C: Number + CheckDigit

file = open("ISBNPRE.txt", "r") 
ISBNList = file.readlines()
for x in range(len(ISBNList)):
    if ISBNList[x][-1:]=='\n':
        new = ISBNList[x][:-1]
        ISBNList[x]=new

def CalCheckDigit(number, total):
    if len(number) > 1:
        digit = int(number[0])
        total = total + digit*(len(number)+1)
        newnumber = number[1:]
        checkdigit = CalCheckDigit(newnumber, total)
    else:
        digit = int(number[0])
        total = total + digit*(len(number)+1)
        calcmodulus = total % 11
        checkvalue = 11 - calcmodulus
        if checkvalue == 11:
            return '0'
        else:
            if checkvalue == 10:
                return 'X'
            else:
                return str(checkvalue)
    if len(number) == 9:
        return number+checkdigit
    else:
        return checkdigit

for item in ISBNList:
    print(CalCheckDigit(item, 0))
    
