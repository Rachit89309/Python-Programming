heights = input("Enter all heights separated by space : ")
height_list = heights.split()

count = 0
for height in height_list:
    count += 1
print(count)    
for i in range(count):
    height_list[i] = int(height_list[i])

total = 0
for person in height_list:
    total = total + person
# print(total)
avg =total/count
print(round(avg))
# print(height_list)
