# two identity operators 
# is or is not
a = 5
b = 5
print(a is b)
print(a is not b)
print(id(a))
print(id(b))

c = 4
d = '4'
print(c is d)
print(c is not d)
print(id(c))
print(id(d))


e = 5
print(id(e))
e = 8    # reassign the value of e
print(id(e))
print(e is e)   #  true because both e have the same reassigned value 8
