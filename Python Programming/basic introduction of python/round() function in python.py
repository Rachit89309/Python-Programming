# round(number, number of digits)

print(round(21.3333332, 2))
print(round(7))
print(round(7, 2))
print(round(7.61))
print(round(2.6666, 2))
print(round(2.6657, 0))
print(round(7.5))   # it will return nearest even integer
print(round(6.5))


print(round(665, -1))
print(round(675, -1))  # after getting 0 we have to reach the nearest even integer
print(round(674, 2))
print(round(674, 0))
print(round(674, -1))   # 10 ^ (-no. of digits)
print(round(674, -2))
print(round(634, -2))
print(round(674, -3))   # we suppose a 0 in the first index of number and then solve it
print(round(444, -3))
print(round(500, -3))
print(round(674, -4))


# negative numbers
print(round(-8/3))
print(round(-1.5))
print(round(-8/3, 2))
print(round(6.75, 1))
print(round(6.85, 1))
print(round(674.1012, -1))
print(round(1212, -2))
print(round(467, -3))