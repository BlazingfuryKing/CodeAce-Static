# import random

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


def EAN(ean12):
    # task 2.1
    pass

def EAN_rec(ean12):
    # task 2.2
    pass



def test_21_22():
    print(EAN("400638133393"))#1
    print(EAN("590123412345"))#7
    print(EAN("950110153000"))#3
    print(EAN("007567816412"))#5
    print(EAN("123456789123"))
    print(EAN("563643712973"))

    print(EAN_rec("400638113393"))#7
    print(EAN_rec("590123422345"))#4
    print(EAN_rec("950110133000"))#9
    print(EAN_rec("007567846412"))#6
    print(EAN_rec("123456759123"))
    print(EAN_rec("563643762973"))

#test_21_22()

def generate_n_random_EAN(n):
    # task 2.3
    pass

print(generate_n_random_EAN(5))

def quick_sort_10_EAN():
    # task 2.4
    pass

print(quick_sort_10_EAN())






    
    
