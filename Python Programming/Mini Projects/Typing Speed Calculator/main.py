from time import *
import random as rand

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error                
             

test = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea", 
"My name is Rachit", "Welcome to all in this project"]
test1 = rand.choice(test)
print("      *****typing speed *****")
print(test1)
print()
print()
testinput = input("Enter : ")
 













