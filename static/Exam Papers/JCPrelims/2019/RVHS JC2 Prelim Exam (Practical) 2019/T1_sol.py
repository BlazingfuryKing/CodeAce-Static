import datetime
import random

def read_input_file(filename):
    lst = []
    with open (filename,'r') as f:
        line = f.readline()
        while line:
            if line[-1]=='\n':
                lst.append(line[:-1])
            else:
                lst.append(line)
            line = f.readline()
    f.close()
    return lst
name_lst = read_input_file("names.txt")

def create_student_file(filename, female_count, male_count):
    f = open (filename,'w')
    gender = "F"
    role_lst = ["Coder", "Maker", "Dealer", "Empathizer", "Designer"]
    role_index = 0
    for name in name_lst:
        if random.randint(0,1) == 0:
            if female_count > 0:
                gender = "F"
                female_count -= 1
            else:
                gender = "M"
                male_count -= 1
        else:
            if male_count > 0:
                gender = "M"
                male_count -= 1
            else:
                gender = "F"
                female_count -= 1    
                
        f.write(name+";"+role_lst[role_index]+ ";" + gender + "\n")
        #role_index = (role_index + 1) % len(role_lst)
        role_index = random.randint(0,len(role_lst)-1)
        
    f.close()
    
#create_student_file("student_cid.txt", 33, 17)


#########Task 1.1#########
def read_data(filename):
    lst = []
    with open (filename,'r') as f:
        line = f.readline()
        while line:
            if line[-1]=='\n':
                lst.append(line[:-1].split(";"))
            else:
                lst.append(line)
            line = f.readline()
    f.close()
    return lst

#########Task 1.2#########
def gender_count(cid_student_lst, is_female):
    return len(list(filter(lambda x:x[2]==("F" if is_female else "M"), cid_student_lst)))

cid_student_lst = read_data("student_cid.txt")
print(gender_count(cid_student_lst, True))
print(gender_count(cid_student_lst, False))

#########Task 1.3#########
def role_statistic(cid_student_lst):
    dic = {}
    for name, role, gender in cid_student_lst:
        if role not in dic:
            dic[role] =  1
        else:
            dic[role] +=  1
    result = []
    sorted_role_lst = sorted(dic.keys())

    print("{:15}{}".format("Role", "Number"))
    for role in sorted_role_lst:
        result.append(dic[role])
        print("{:15}{}".format(role, dic[role]))
    
    return result

cid_student_lst = read_data("student_cid.txt")
print(role_statistic(cid_student_lst))

#########Task 1.4#########
def form_random_group(cid_student_lst):
    #return names of a valid group only
    dic = {}
    result = []
    for name, role, gender in cid_student_lst:
        if role not in dic:
            dic[role] = [name,]
        else:
            dic[role].append(name)
    
    sorted_role_lst = sorted(dic.keys())

    for role in sorted_role_lst:
        if role in ["Coder", "Maker", "Dealer", "Empathizer", "Designer"]:
            num_student = len(dic[role])
            result.append(dic[role][random.randint(0,num_student-1)])
    if len(result) == 5:
        return result
    else:
        return []

cid_student_lst = read_data("student_cid.txt")
for i in range(3):
    print(form_random_group(cid_student_lst))

#########Task 1.5#########
def remove_students(cid_student_lst, one_cid_group):
    # remove records in cid_student_lst based on the name in one_cid_group
    # return the removed records as a list
    removed_records = []
    removed_index_lst = []
    for i in range(len(cid_student_lst)):
        if cid_student_lst[i][0] in one_cid_group:
            removed_index_lst.append(i)
    count = 0
    for index in removed_index_lst:
        removed_records.append(cid_student_lst.pop(index - count))
        count += 1
    return removed_records

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
    all_groups = []
    one_cid_group_name_lst = form_random_group(cid_student_lst)
    while one_cid_group_name_lst:
        removed_record = remove_students(cid_student_lst, one_cid_group_name_lst)
        all_groups.append(removed_record)
        one_cid_group_name_lst = form_random_group(cid_student_lst)

    f = open ("result.txt",'w')
    for i in range(len(all_groups)):
        f.write("Group " + str(i) + '\n')
        for name, role, gender  in all_groups[i]:
            f.write(name + " " + role+ " " + gender + '\n')
    
    f.close()

form_max_cid_group(cid_student_lst)

    




    
