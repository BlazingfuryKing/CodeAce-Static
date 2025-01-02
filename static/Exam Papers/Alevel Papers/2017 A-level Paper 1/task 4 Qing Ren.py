import random
def display(lst):
    for row in lst:
        count = 0
        for letter in row:
            print(letter, end = '')
            print(' ', end = '')
            count += 1
            if count == 4:
                print('\n')
    return lst


def transform_1(lst):
    x = random.choice([1,2])
    if x == 1:
        n1 = 0
        n2 = 1
    else:
        n1 = 2
        n2 = 3
    lst[n1],lst[n2] = lst[n2], lst[n1]
    return lst

def transform_2(lst):
    x = random.choice([1,2])
    if x == 1:
        n1 = 0
        n2 = 1
    else:
        n1 = 2
        n2 = 3
    for row in lst:
        row[n1], row[n2] = row[n2], row[n1]
    return lst

def transform_3(lst):
    lst[0], lst[1], lst[2], lst[3] = lst[2], lst[3], lst[0], lst[1]
    return lst

def transform_4(lst):
    for row in lst:
        row[0], row[1], row[2], row[3] = row[2], row[3], row[0], row[1]
    return lst


def ran_transforms(lst):
    return random.sample(lst,2)

transforms = [transform_1, transform_2, transform_3, transform_4]
lst = [[4,3,2,1],[1,2,4,3],[3,4,1,2],[2,1,3,4]]

for fn in ran_transforms(transforms):
    print('before:')
    display(lst)
    lst = fn(lst)
    print('after:')
    display(lst)
    

              

