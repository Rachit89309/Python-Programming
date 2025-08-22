def greet(name):
    print(f"Hi {name}")
    print("Are you from CS department")
greet("Rachit") 

# difference between argument and parameter
# A parameter is the variable listed inside the parentheses in the function definition. 
# An argument is the value that are sent to the function when it is called.

def add(a, b):
    c = a + b
    print(f"Sum is {c}")
add(5, 7)   


# types of arguments ->
# 1) default, 2) positional, 3) keyword, 4) arbitrary
def greeting(name1, subject, dept = "CS"):
    print(f"Hi {name1}")
    print(f"Do you teach {subject}?")
    print(f"Are you from {dept} department?")
greeting("Rachit", "Python")   



#  *args-> this is short form of arbitrary positional argument
#  and **kwargs -> short form for arbitrary keyword argument

def add(*numbers):
    c = 0
    for i in numbers:
        c += i
    print(f"Sum is {c}")

add(1, 2)
add(1, 2, 3, 4, 56, 8)        


def info_person(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs) 




info_person(name = "Ram", age = 30, dept = "CSE")
info_person(name = "Shyam", dept = "CSE")

# how to use ceil() function -> ceil() function is used to return the ceiling value of a number, 
# which means it is used to round a number up to the nearest integer that is greater than the number itself.
#  For example, the math. ceil() of 6.3 is 7, and the math. ceil() of -10.7 is -10.