#1) Create a program to read text lines from the keyboard input and append them at the end of a text file.
import sys

if len(sys.argv) < 2:
    print("Not enough arguments: Please write a valid text filename")
    sys.exit()

try: 
    myfile = open(sys.argv[1], "a")
except FileNotFoundError:
    print("The given file does no exist")
else:
    user_text = None
    while user_text != "*":
        user_text = input("Enter text (* to exit): ")
        if user_text != "*":
            myfile.write(user_text + '\n')

myfile.close()








