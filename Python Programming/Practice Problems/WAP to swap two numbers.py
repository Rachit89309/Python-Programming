a = input("Enter value of a = ")
b = input("Enter value of b = ")
# using a temporary variable to hold the value of a
temp = a
# assigning the value of b to a
a = b
# assigning the value stored in temp to b 
b = temp

# printing the swapped values of a and b
print("a=" + a)
print("b=" + b)

# ex. ->  let a = 5
# b = 10
# temp = 5
# a = 10
# b = 5


#   Another approach

# Taking input for variables 'a' and 'b'
c = int(input("Enter value of c = "))
d = int(input("Enter value of d = "))

# Swapping without a temporary variable
c = c + d  # Sum of both numbers is stored in 'a'
d = c - d  # Subtracting 'b' from the sum gives the original value of 'a', stored in 'b'
c = c - d  # Subtracting the new value of 'b' from the sum gives the original value of 'b', stored in 'a'

# Printing the swapped values
print("c=" + str(c))
print("d=" + str(d))

# this approach is more efficient since it eliminates the need for a 
# temporary variable. However, it works best with numbers and not strings.
