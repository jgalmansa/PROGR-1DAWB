#5) Write a program that creates a copy of a file (the names of the original file and the copy will be passed as a parameter on the command line).

import sys

if len(sys.argv) < 3:
    print("Syntax: ")
    print(sys.argv[0], " <file1> <new file2>")
    sys.exit()


try:
    file1 = open(sys.argv[1], 'rb')
except FileNotFoundError:
    print("The given file does not exist")
else:
    content = file1.read()
    file2 = open(sys.argv[2], "wb")
    file2.write(content)

file1.close()
file2.close()







