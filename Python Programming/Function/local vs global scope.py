# Local variables are defined inside a function or block, whereas global variable is defined outside of all functions or blocks. 
# Local variables exist only during the function's executions, while global variables remain in memory for the duration of the program.

a= 10   # global scope
def display():
    a = 15   # local scope     # we can not define a variable inside a function
    def show():   #
        print(a)
    show()        
display()

print(a)    