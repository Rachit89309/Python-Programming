#  f-strings (formatted string literals) are a way to embed expressions inside string literals in Python, using curly braces {}.

name = 'Krishna'
age = 30
height = 1.6
print("My name is : " +name, "I am " +str(age),"years old")
# or
print("My name is : ", name, "I am ", age, "years old")
# what if i put all in single quote
# it so simple to making the string f-string by using the curly braces
print(f"My name is {name}. I am {age} years old. My height is {height}meters")
print(f"Krishna's father is {age*2} years old.")
