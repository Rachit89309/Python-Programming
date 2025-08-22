# loop -> repeat the same action again and again
names = ['jenny', 'ram', 'shyam']
for i in names:
    print(i)
    if i == 'jenny':
        print("Hey, It's me")

numbers = [2, 3, 5, -2, 10] 
squares = []
for i in numbers:
    square = i**2
    squares.append(square)
print(squares)       