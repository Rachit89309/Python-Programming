# it is in-built module in python
#   first of all we have to write import random 
# randint(a, b)   it will random integer no. between a and b and also include both a and b
# a <=  X <= b
# randrange(a, b)  it wil also return random integer no. but it only include a    a <= X < b
# random()   it will return floating point no. range between 0.0.mto 1.0
# 0.0 <= x < 1.0

# uniform()   it will also return floating point no. but it will ocurr in particular range
# choice()   if you want to select random item from a sequence
# shuffle()   if you want to shuffle any sequence

import random


a = random.randint(1, 3)
print(a)

b = random.randrange(1, 3)
print(b)

c = random.random()
print(c)

d = random.uniform(1, 3)
print(d)

l = [2, 5, 90, -5, 89, 12, 56]
e = random.choice(l)
print(e)
f = random.shuffle(l)
print(l)