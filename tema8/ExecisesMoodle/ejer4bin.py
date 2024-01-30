#Binary version
#4) Write two programs that compare two files (to be passed as parameter on the command line)  and determine whether these files have the same content (i.e., whether they are the same or not). Make a first version for text files and a second one for any type of file.


import sys

if len(sys.argv) < 3:
    print("Syntax: ")
    print(sys.argv[0], " <binary file1> <binary file2>")
    sys.exit()

try:
    file1 = open(sys.argv[1], 'rb')
    file2 = open(sys.argv[2], 'rb')
except FileNotFoundError:
    print("The given files do not exist")
else:
    content1 = file1.read()
    content2 = file2.read()

    if content1 == content2:
        print("The files are equal")
    else:
        print("The files are different")

file1.close()
file2.close()

