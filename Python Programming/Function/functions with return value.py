def add(a, b):
    c = a + b
    print(c)
    
add(5, 4)   

# 2nd method
def add1(a, b):
    c = a + b
    return(c)
    
print(add1(5, 4)) 

# 3rd method
def add2(a, b):
    c = a + b
    return(c)
    
result = add2(5, 4)   
print(result) 

# 4th method
def add3(a, b):
    return a + b
    
    
result1 = add3(5, 4) 
print(result1) 


# if return value is not present, it will print None
def sum(a, b):
    c = a + b
    return
    
ans = add(5, 4)
print(ans) 


# to print in the form of title case
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    print(f"{formatted_f_name, formatted_l_name}")  
    
format_name("rachit", "KUMAR")    
    
     