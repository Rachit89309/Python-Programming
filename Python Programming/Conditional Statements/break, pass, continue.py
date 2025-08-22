num = 1
while(num <=10):
    if num %2 != 0: # num is odd
        num += 1 # go to the next natural number
        continue # go to the nearest loop
    print(num)
    num += 1

# break means exit from the loop immediately
list1 = ["hi", "Hello", "Welcome"]
names = ["Krishan", "Ram", "Madhav"]
for item in list1:
    for name in names:
        print(item, name)
        if item == "Hello" and name == "Ram":
            break 
    print("out from inner loop")
print("out from outer loop")   


# continue statements is used to skip the remaining code inside a loop for the current iteration only.
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 7:
        continue
    print("Hi")
print("out from loop")   


# pass statement -> The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
total = 1
while total <= 10:
    print(total)
    total += 1
    if total == 7:
        pass
    print("Hello World")
print("Out from loop")    