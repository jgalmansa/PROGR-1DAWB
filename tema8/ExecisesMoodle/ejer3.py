# 3) Write a program that takes one word and replaces it with another in a text file.

import sys

if len(sys.argv) < 4:
    print("Syntax: ")
    print(sys.argv[0], " <filename> <word1: new word> <word2: replaced word>")
    sys.exit()

try:
    my_file = open(sys.argv[1], 'r')
except FileNotFoundError:
    print("The given file does no exist")
else:
    lines = []
    for line in my_file:
        new_line = line.replace(sys.argv[3], sys.argv[2])
        lines.append(new_line)
my_file.close()

my_file = open(sys.argv[1], 'w')
my_file.writelines(lines)
my_file.close()


