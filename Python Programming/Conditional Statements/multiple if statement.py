height = int(input("Enter your height : "))
if height >= 3:
    print("Can ride")
    age = int(input("What is your age?"))
    
    
    if age < 12:
        bill = 150
        print("Ticket Price is 150 Rs.")
    elif age <= 18:
        bill = 250
        print("Ticket Price is 250 Rs.")
    else:
        bill = 500
        print("Ticket Price is 500 Rs.")

    want_photo = input("Do you want to take photo(Y/N)? ")
    if want_photo =='Y':
       bill = bill + 50 
    else:
        bill       

    print(f"Your total bill is {bill}")
else:
    print("Can't ride") 
print("Thank you ... Enjoy the Ride !!")                