a = 10  # global
def display():
    # a = 15  # local
    global a # if you modify a global variable you can define global keyword
    a= a + 1 # you can not modify the value without defining it globally
    print(a)
display()
print(a) 



name = "Rachit"
def show():
    global name
    name = name + "Kumar"
print(name)
show()
print(name)       