# open mode
# f = open("file.txt")

# First create the file
f = open("text.txt", "w")
f.write("Hello, this is a test file.")
f.close()

# read = "r"
# write = "w"
f = open("text.txt", "r")
content = f.read()
print(content)
f.close()

""" Adding text, counting characters
Append function-
helps us to add text in your .txt file. 
the mode used is "a" for appending means adding or writing some text to the file. 
for adding text to the file in a new line use \n before writing the sentence to be added 

Len function - 
to count the characters in a text file len() is the function used 
firstly we open the file and read that using the functions 
and after the reading of the text len function is assigned with the variable to find the count of characters """

# append - "a"
f = open("text.txt", "a")
add_text = f.write("\nThis is a append mode")
print(add_text)
f.close()

# len function
f = open("text.txt", "r")
data_read = f.read()
total_count = len(data_read)
print("Total characters in the file:", total_count)
f.close()


'''
Readline Function-
This readline function helps us to read the text line by line
For using this function, firstly open file is needed and in whatever way you want you can open the file, either read or write 
Then accordingly used the readline function to read the lines accordingly in the form of line by line'''

f = open("text.txt", "w")
f.write("I am learning file handling")
f.write("\nTopics are in open, read and append mode")
f.write("\nappend function")

# Closing the file after writing
f.close()

# Reading lines one by one
f = open("text.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()