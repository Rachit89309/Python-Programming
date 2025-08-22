height = int(input("Enter your height in feet : "))
# if height >= 3:
#     print("You can ride")
#     age = int(input("What is your age ? "))
#     if age <= 18:
#         print("Pay Rs.250")
#     else:
#         print("Pay Rs.500")
# else:
#     print("You cannot ride")    

# print("Bye") 


if height >= 3:
    print("You can ride")
    age = int(input("What is your age ? "))
    if age < 12:
        print("Pay Rs.150")
    elif age <= 18:
        print("Pay Rs.250")
    else:
        print("Pay Rs.500")     
else:
    print("You cannot ride") 
