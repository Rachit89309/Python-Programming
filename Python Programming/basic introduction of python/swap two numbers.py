a = int(input("Enter value of a : "))
b = int(input("Enter valuue of b : "))
temp = a     # temp is a variable in which we store a and b
a = b
b = temp
print("a =", a)   # you can also use + (operator) instead of commas 
print("b =", b)