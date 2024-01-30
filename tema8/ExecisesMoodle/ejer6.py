#6) Write a program that asks as an integer (via the command line) between 1 and 10 and saves in a file named table-n.txt the multiplication table of that number, where n is the number entered.

import sys

MAX_VALUE = 10

if len(sys.argv) < 2:
    print("Syntax: ")
    print(sys.argv[0], " <integer> ")
    sys.exit()

try:
    number = int(sys.argv[1])
except ValueError:
    print("Please enter a valid integer number")
    sys.exit()

if number < 1 or number > 10:
    print("Enter an integer number between 1 and 10")
    sys.exit()


fileName = "table-" + str(number) + ".txt"
file = open(fileName, "w")

for i in range(0,MAX_VALUE+1):
    product = number * i
    file.write(str(number) + " * " + str(i) + " = " + str(product) + "\n")


file.close()





