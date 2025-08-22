'''
Try and Except Statement-
the code written inside the try block executes if the code is error free. 
if the code is not error free then the except block gets executed and results an exception
a try statement can have more than one except statement  

syntax - 
        try:
            statement
        except:
            exception    
'''

a = input("Enter the number 1: ")
b = input("Enter the number 2: ")

try:
    # unsupported operand type(s) for +: 'int' and 'str'
    c = int(a) + int(b)
    print(c)

except:
    print("Error in your try block")  


'''
Try with else clause -
Else clause is used with the try clause when you want to execute the set of instructions in the absence of exceptions in your code'''

c = int(input("Enter the number 3: "))

try:
    if c % 2 == 0:
        print(f"{c} is an even number")
    else:
        print(f"{c} is an odd number")

except Exception as e:
    print(e)
else:
    print("Else clause got executed")  


'''
Finally Keyword -
Finally is a keyword which surely executes after the execution of the try and except block of statement''' 

x = int(input("Enter number 5: "))
y = int(input("Enter number y: "))

try:
    if x > y:
        print(f"{x} is greater than {y}")
    else:
        print(f"{y} is greater than {x}")  

except Exception as e:
    print(e) 

finally:
    print("Finally keyword used")