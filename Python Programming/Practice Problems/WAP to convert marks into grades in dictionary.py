student_marks = {
    "Jenny": 92,
    "Harry": 78,
    "Dimpy": 56,
    "Rahul": 41,
    "Aniket": 99,
    "Prem": 34
}

student_grade = {}
for student in student_marks:
    marks = student_marks[student]
    if marks > 90:
        student_grade[student] = "A+"
    elif marks > 80:
        student_grade[student] = "A" 
    elif marks > 70:
        student_grade[student] = "B+"  
    elif marks > 60:
        student_grade[student] = "B"  
    elif marks > 50:
        student_grade[student] = "C"  
    elif marks > 40:
        student_grade[student] = "D"
    else:
        student_grade[student] = "F"
        
print(student_grade)        
                                