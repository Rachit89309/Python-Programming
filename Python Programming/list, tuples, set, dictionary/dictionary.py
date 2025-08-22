#  it is used to store the data in the form of key value pairs.
# duplicate entries are not allowed
# it is a mutable function means we can change it


phone_no = {
    'Ram': 1234,
    'Shyam': 345,
    'Mohan': 8976
}
print(phone_no)
print(phone_no['Shyam'])
phone_no['Mohan'] = 9999
print(phone_no)
print(phone_no['Ram'])

# using get method
# if the key does not match with the dictionary it shows None rather than error
print(phone_no.get('Mohan'))
print(phone_no.get('mohan'))


# deleting the element in dictionary
del phone_no['Ram']
print(phone_no)








# other method for creating a dictionary
# in a dictionary other dictionary also allowed means nested dictionary
number = dict({
    'shiv': 1234,
    'sam': 6585,
    'maddy': 6798
})
print(number)
number['shiv'] = {1111, 2222, 3333}
print(number)

print(number.keys())
print(number.values())
print(number.items())

for i in number:
    print(i)
    print(number[i])
    
    
for i in number.items():
    print(i)   
    

print(phone_no) 
phone_no2 = phone_no.copy() 
print(phone_no2)  

print(len(number))
     