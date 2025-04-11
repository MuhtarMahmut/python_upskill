
student1 = {}

print(type(student1))

student1["student_name"] = "Ali"
student1["student_name"] = "Said"
student1["age"] = 30
student1["gpa"] = 3.5
student1["full_time"] = True
print(student1)

student1["gpa"] = 4.5

print(student1)

student1.pop("age")

print(student1)

student1.popitem()
print(student1)

# print(help(dict.pop))

# print( help(dict.popitem) )

print(student1["gpa"])

print("---------------------------------")

employee1 ={
    "employee_name": "Bahadir",
    "employee_id": "A123",
    "employee_salary": 100_000,
    "full_time": True,
    "job_title": "Python Developer"
}

for each_key in employee1.keys():
    # print(each_key)
    # print(employee1[each_key])
    print(f'{each_key} ==> {employee1[each_key]}')

print("---------------------------------")

for each_pair in employee1.items():
    # print(each_pair)
    print(f"{each_pair[0]} ====> {each_pair[1]}")

print("------------------------")

employee2 ={
    "employee_name": "Naila",
    "employee_id": "A124",
    "employee_salary": 120_000,
    "full_time": False,
    "job_title": "Project Manager"
}

employee3 ={
    "employee_name": "Said",
    "employee_id": "A125",
    "employee_salary": 110_000,
    "full_time": True,
    "job_title": "SDET"
}


employees = [employee1, employee2, employee3]

for each_dict in employees:
    print("=================================================================")
    for each_pair in each_dict.items():
        print(f"{each_pair[0]}  ====> {each_pair[1]}")




