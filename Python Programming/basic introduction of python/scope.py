a4 = 13  # Global variable a4 is set to 13
  # Prints 13

def f4():
    global a4
    a4 = 12  # Modifies the global variable a4 to 12
    print(a4)  # Prints 12
    print(id(a4))  # Prints the ID of the modified a4 (12)

print(a4)  # Prints 13 (before calling f4)
f4()  # Calls f4, which changes a4 to 12 and prints 12 and its ID
print(a4)  # Prints 12 (after calling f4)
print(id(a4))  # Prints the ID of the modified a4 (12)
