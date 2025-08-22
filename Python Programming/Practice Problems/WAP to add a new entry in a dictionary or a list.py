student_data = [
    {
        "Name" : "Ram",
        "roll_no" : 10,
        "age" : 20,
        "course" : "Python"    
    },
    {
        "Name" : "Mohan",
        "roll_no" : 20,
        "age" : 22,
        "course" : "Java" 
    }
]
def add_new_student(name, rollno, age, course):
    new_student = {}
    new_student["Name"] = name
    new_student["roll_no"] = rollno
    new_student["age"] = age
    new_student["Course"] = course
    student_data.append(new_student)
    
add_new_student("Shyam", 22, 18, "C++")
print(student_data)