#7) Write a program that asks as an integer (via the command line) between 1 and 10, then read the file table-n.txt with the multiplication table of that number, where n is the number entered. If the file does not exist it should display a message on the screen reporting about it.

import sys

MAX_VALUE = 10

if len(sys.argv) < 2:
    print("Syntax: ")
    print(sys.argv[0], " <integer> ")
    sys.exit()

number = int(sys.argv[1])
if number < 1 or number > 10:
    print("Enter an integer number between 1 and 10")
    sys.exit()

fileName = "table-" + str(number) + ".txt"
try:
    file = open(fileName)
except FileNotFoundError:
    print("The file with the multiplication table of ", number, " does not exist")
    sys.exit()
else:
    content = file.read()
    print(content)


file.close()






