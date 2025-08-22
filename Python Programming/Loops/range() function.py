# range(start, end, step)   by default start is o and end is compulsory, by default step size is 1 but it is optional.
a = range(5)
print(a[0])
print(a[1])

b = range(2, 5)
for i in b:
    print(i)


c = range(2, 15, 2)
for i in c:
    print(i)

d = range(2, 15, -3) 
for i in d:
    print(i)  

# e = range(2, 15, 0) 
# for i in e:
#     print(i)      it gives value error because in range function argument 3 must not be zero



total = 0
for i in range(1, 101):
    total += i
print(total)    