#8) Write a program that asks for two numbers  n and m between 1 and 10 from the command line, then read the table-n.txt file and finally retrieves and displays the line with the outcome of n x m.

import sys

MAX_VALUE = 10

if len(sys.argv) < 3:
    print("Syntax: ")
    print(sys.argv[0], " <integer> <integer>")
    sys.exit()

number1 = int(sys.argv[1])
number2 = int(sys.argv[2])
if (number1 < 1 or number1 > 10) or (number2 < 1 or number2 > 10):
    print("Enter two integer numbers between 1 and 10")
    sys.exit()

fileName = "table-" + str(number1) + ".txt"
try:
    file = open(fileName)
except FileNotFoundError:
    print("The file with the multiplication table of ", number1, " does not exist")
    sys.exit()
else:
    lines = file.readlines()
    file.seek(0)
    for num, line in enumerate(lines):
        if num == number2:
            print(line)


file.close()












