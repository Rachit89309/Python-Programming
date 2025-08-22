#datatype -> it tells the types of data stored in variable
# but in python it is different from other languages 
# as we know that python is object oriented programming language so everything is considered like as an object
# so in this case these datatypes are considered as classes and variables created are considered as instance

# type() function is used to check the datatype of variable
# it will give output   <class 'int'>


#types of primitive datatype --> int, float, string, boolean etc.
#int
var_1 = 3
print(var_1)
print(type(var_1))

# float
var_3 = 123
var_2 = 10.1
var_4 = var_3 + var_2
print(var_4)
print(type(var_4))


var_1 = 0o123    # octal
var_2 = 0x123    # hexadecimal
print(var_1)
print(var_2)



# strings
name = "Rachit Kumar"
print(type(name))
print(name[5])

print("Jenny\'s \n \"Lectures\"")
print(5 * "Jenny\'s \n \"Lectures\"")


# boolean
var = True
print(var)
print(type(var))


a = 1
b = 2
var = a < b
print(var)
