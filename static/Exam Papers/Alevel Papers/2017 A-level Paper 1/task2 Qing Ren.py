#task 2.1
#A CalCheckDigit(NewNumber, Total)
#B RETURN STRING(X)
#C Return Number + string(checkdigit) else return checkdigit

def CalCheckDigit(Number,Total):
    if len(Number) > 1:
        Digit = int(Number[0])
        Total = Total + Digit * (len(Number) + 1)
        NewNumber = Number[1:]
        CheckDigit = CalCheckDigit(NewNumber, Total)
    else:
        Digit = int(Number[0])
        Total = Total + Digit * (len(Number) + 1)
        CalcModulus = Total % 11
        CheckValue = 11 - CalcModulus
        if CheckValue == 11:
            return '0'
        else:
            if CheckValue == 10:
                return 'X'
            else:
                return str(CheckValue)
    if len(Number) == 9:
        return Number + str(CheckDigit)
    else:
        return str(CheckDigit)

file1 = open('ISBNPRE.txt')
lst = file1.read().splitlines()
for line in lst:
    print(CalCheckDigit(line, 0))
