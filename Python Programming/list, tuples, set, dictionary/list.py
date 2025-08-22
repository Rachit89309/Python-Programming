# mutable - can change means after creating the list we can modify it
# list can have duplicate value

number = [10, 0, -1, 7]
names = ['Jenny', 'Krishna', 'Ram']
mix_list = [1, 'Jenny', True, 10.10]
print(number[1])
print(len(names))


# negative indexing
print(mix_list[-2])

# slicing
print(number[1:])
print(number[: 3])
print(number[1:3])

numbers = [10, 0, -1, 7, 8, 10, -67]
print(numbers[0:8:2])
print(numbers[0::3])

numbers.sort()
print(numbers)
print(numbers.sort())    # it will print None
numbers.reverse()
print(numbers)
print(max(numbers))
print(min(numbers))

mix_list.append(84)
print(mix_list)

numbers.insert(4, 34)
print(numbers)

# add more than one data at a time
numbers.extend([45, 46, 47, 78, 89])
print(numbers)


numbers[1] = 93
print(numbers)

numbers[1:4] = [45, 46, 47]
print(numbers)


# remove
numbers.remove(0)
print(numbers)

numbers.remove(45)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.pop(5))
print(numbers)