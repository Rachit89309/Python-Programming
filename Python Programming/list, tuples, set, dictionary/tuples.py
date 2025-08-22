#  tuples are used to store multiple values in a single variable name
# uses round brackets ()
# mixed datatypes are possibles
#  in tuple no single value is valid    for this we have to add comma after that
# e.g - tuple = (10,)

# tuple = (12, 6, -8, "Jenny", True)
tuple1 = (10)
# indexing
print(tuple[2])
print(tuple)
print(type(tuple))
print(type(tuple1))
tuple2 = (10,)
print(type(tuple2))

# tuples are immutable means it is not changeable

# tuple does not support item assignment
#tuple[0] = 13
print(tuple)

# duplicates items are allowed
# concatenation of tuple
# here tuple3 is nested tuple
tuple3 = (tuple1, tuple2)
print(tuple3)

# in mixed datatypes min and max function are not working


# convert list into tuples
list_ =[1, 2, 3, 4]
tuple4 = tuple(list_)
print(tuple4)

