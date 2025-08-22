length = len("Rachit Kumar")
print(length)
print(len("12345"))    # object of type 'int' has no len()    len(12345)  --> it will give type error

# len function is only used for string only

# print("Your name has" + length + "character")
# it will give type error because it can only concatenate str (not "int") to str

print("Your name has " + str(length) + " character")
new_length = str(length)
print(type(new_length))
print(type(length))
print("10" + "10")
print(int("10") + int("10"))
print(10 + float("10"))


# assignment
first_number = input("Enter first number : ")
second_number = input("Enter second number : ")
sum = int(first_number) + int(second_number)
print(sum)

# Typecasting, also known as type conversion, is the process of converting one data type to another. In Python, this can be done explicitly using built-in functions. Typecasting is useful when you need to perform operations that require operands of the same type or when you want to convert data to a different format for compatibility or other reasons.
