# The alphabet list contains all the lowercase letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Function to encrypt plain text
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        # check if the character is in the alphabet
        if char in alphabet:
            # get the position of the character in the alphabet
            position = alphabet.index(char)
            # calculate the new position after shifting
            new_position = (position + shift_key) % 26
            # add the encrypted character to cipher_text
            cipher_text += alphabet[new_position]
        else:
            # if the character is not in the alphabet, add it as is
           cipher_text += char 
    # print the encrypted text        
    print(f"Here's is the text after encryption : {cipher_text}")
def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        # check if the character is in the alphabet
        if char in alphabet:
            # get the position of the character in the alphabet
            position = alphabet.index(char)
            # calculate the original position by shifting backwards
            new_position = (position - shift_key)%26
            # add the decrypted character to plain_text
            plain_text += alphabet[new_position]
        else:
            # if the character is not in the alphabet, add it as is 
            plain_text += char
    # print the decrypted text        
    print(f"Here's is the text after decryption : {plain_text}")        
         
 # flag to control the loop for repeated encryption/decryption       
wanna_end = False

# loop until the user decides to stop
while not wanna_end:
    # ask the user if they want to encrypt or decrypt
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption : ")
    # get the text to encrypt or decrypt
    text = input("Type your message : \n").lower()
    # get the shift key from the user
    shift = int(input("Enter shift key : \n"))
    
    # perform the operation based on user choice
    if what_to_do == "encrypt":
        encryption(plain_text = text, shift_key = shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text = text, shift_key = shift)
        
    # ask the user if they want to continue or exit    
    play_again = input("Type 'yes' to continue type 'no' to exit : ")
    
    # if the user types 'no' end the loop
    if play_again == 'no':
        wanna_end = True
        print("Have a nice day! Bye..")
    

    
        