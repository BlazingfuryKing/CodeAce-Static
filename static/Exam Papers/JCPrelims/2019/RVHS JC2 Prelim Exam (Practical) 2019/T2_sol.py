import random

# EAN-13 barcode a standard describing a barcode symbology
# and numbering system used in global trade to identify a
# specific retail product type, in a specific packaging configuration,
# from a specific manufacturer.
#
# EAN (European Article Number) check digits (administered by GS1)
# are calculated by summing each of the odd position numbers multiplied by 3
# and then by adding the sum of the even position numbers.
# Numbers are examined going from right to left,
# so the first odd position is the last digit in the code.
# The final digit of the result is subtracted from 10 to
# calculate the check digit.

# Implementa an iteravtive function EAN that takes in a string ean12 which
# is the first 12 characters of a valid EAN number and return the 
# full valid EAN with check digit in string

def EAN_rec(ean12):
    def EAN_helper(ean_str, isTriceWeight):
        if len(ean_str) == 1:
            return int(ean_str)
        else:
            if isTriceWeight:
                return int(ean_str)*3 + EAN_helper(ean_str[:-1], False)
            else:
                return int(ean_str) + EAN_helper(ean_str[:-1], True)
    total = EAN_helper(ean12, True)
    check_dight = 10 - total % 10
    if check_dight == 10:
        return ean12 + "0"
    else:
        return ean12 + str(check_dight)

def EAN(ean12):
    total = 0
    for i in range(len(ean12)-1, -1, -1):
        if i % 2 == 1:
            total += int(ean12[i])*3
        else:
            total += int(ean12[i])
    check_dight = 10 - total % 10
    if check_dight == 10:
        return ean12 + "0"
    else:
        return ean12 + str(check_dight)

def test_31():
    print(EAN("400638133393"))#1
    print(EAN("590123412345"))#7
    print(EAN("950110153000"))#3
    print(EAN("007567816412"))#5
    print(EAN("123456789123"))#1
    print(EAN("563643712973"))#8

    print(EAN_rec("400638113393"))#7
    print(EAN_rec("590123422345"))#4
    print(EAN_rec("950110133000"))#9
    print(EAN_rec("007567846412"))#6
    print(EAN_rec("123456759123"))#0
    print(EAN_rec("563643762973"))#3



test_31()

def generate_n_random_EAN(n):
    result = []
    for i in range(n):
        ean = random.randint(0, 999999999999)
        padding = 12 - len(str(ean))
        ean12str = "0"*padding + str(ean)
        result.append(EAN(ean12str))
    return result

print(generate_n_random_EAN(50))

def quick_sort(ean_lst):
    #quick sort
    if len(ean_lst) == 0:
        return []
    else:
        smaller = []
        larger = []
        pivot = ean_lst[0]
        count = 1
        for i in range(1, len(ean_lst)):
            if ean_lst[i] > pivot:
                larger.append(ean_lst[i])
            if ean_lst[i] < pivot:
                smaller.append(ean_lst[i])
            if ean_lst[i] == pivot:
                count += 1
        return quick_sort(smaller) + [pivot,]*count + quick_sort(larger)

def quick_sort_10_EAN():
    return quick_sort(generate_n_random_EAN(10))

print(quick_sort_10_EAN())






    
    
