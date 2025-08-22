import statistics
def mean_median_mode(list1):
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)

print(mean_median_mode([3, 5, 45, 3, 2, 1, 89]))


# 2nd method
a, b, c = (mean_median_mode([3, 5, 45, 3, 2, 1, 89]))
print(f"Mean is {a}, Median is {b}, Mode is {c}")



def add(x, y):
    if x == 0 & y == 0:
        return
    else:
        return x + y
    
var1 = int(input("Enter first variable :\n"))
var2 = int(input("Enter second variable :\n"))
result = (add(var1, var2))
print(result)    