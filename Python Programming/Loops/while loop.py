count = 1
while count <= 5:
    print(count)
    count += 1
    if count == 3:
        break
else:
    print("An else block")
print("out from loop")


# Sentinal Value -> Sentinel Value examples include -1, null, or other unique values that are unlikely to occur within the dataset.
number = int(input("Enter a number(-1 to quit): "))
while number != -1:
    print(number)
    number = int(input("Enter a number(-1 to quit)"))
else:
    print("in else block")
print("out from loop")        
    
