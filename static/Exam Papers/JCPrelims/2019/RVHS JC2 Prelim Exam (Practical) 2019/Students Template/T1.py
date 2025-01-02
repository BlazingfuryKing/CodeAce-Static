import random

#########Task 1.1#########
def read_data(filename):
    pass

#########Task 1.2#########
def gender_count(cid_student_lst, is_female):
    pass

print("------Task 1.2------")
cid_student_lst = read_data("student_cid.txt")
print(gender_count(cid_student_lst, True))
print(gender_count(cid_student_lst, False))

#########Task 1.3#########
def role_statistics(cid_student_lst):
    pass

print("------Task 1.3------")
cid_student_lst = read_data("student_cid.txt")
print(role_statistics(cid_student_lst))

#########Task 1.4#########
def form_random_group(cid_student_lst):
    pass

print("------Task 1.4------")
cid_student_lst = read_data("student_cid.txt")
for i in range(3):
    print(form_random_group(cid_student_lst))

#########Task 1.5#########
def remove_students(cid_student_lst, one_cid_group):
    # remove records in cid_student_lst based on the name in one_cid_group
    # return the removed records as a list
    pass

def test_15():
    print("------Task 1.5------")
    cid_student_lst = read_data("student_cid.txt")
    one_cid_group = form_random_group(cid_student_lst)
    removed_records = remove_students(cid_student_lst, one_cid_group)
    print("removed records")
    for removed_record in removed_records:
        print(removed_record)
    print("remaining records")
    for cid_student in cid_student_lst:
        print(cid_student)

test_15()

#########Task 1.6#########
def form_max_cid_group(cid_student_lst):
    pass

cid_student_lst = read_data("student_cid.txt")
form_max_cid_group(cid_student_lst)

    




    
