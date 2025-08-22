# a dictionary within a dictionary

student_data = {
    "Ram" : {"roll_no" : 10, "age" : 20, "course" : "Python"},
    "Mohan" : {"roll_no" : 20, "age" : 22, "course" : "Java"}
}

print(student_data)
print(student_data["Mohan"])
# print(student_data["Mohan"]["roll_no"])

# for updation
student_data["Mohan"]["phone_no"] = 893094
print(student_data["Mohan"])

# for deleting
del student_data["Mohan"]["phone_no"]
print(student_data["Mohan"])