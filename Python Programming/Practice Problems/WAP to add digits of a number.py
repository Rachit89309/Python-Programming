number = input("Enter a two digit number : ")
first_digit = number[0]
second_digit = number[1]
print(int(first_digit) + int(second_digit))




# WAP to add a multiple digit number
number_1 = input("Enter a number with multiple digits: ")
# Initialize a variable to store the sum of digits
digit_sum = 0

# Loop through each character in the string
for digit in number_1:
    digit_sum += int(digit)  # Convert each character to an integer and add to the sum

# display the final sum of the digits
print(f"The sum of the digits of {number_1} is {digit_sum}")