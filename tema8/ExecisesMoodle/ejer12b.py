"""
12) Given a text file that stores in the first line the dimensions of the matrix (rows and columns) and in consecutive lines the elements of the matrix:
  3 4
  2 0 3 -1
  3 -2 10 9
  5 1 7 7
    a) Write the code for a program that reads a matrix from the file.
    b) Write code for a program that writes an array to the file.
"""

import sys

if len(sys.argv) < 2:
    print("Syntax: ")
    print(sys.argv[0], " <matrix text filename> ")
    sys.exit()

matrix = [
    [2,0,3,-1],
    [3,-2,10,9],
    [5,1,7,7],
]


with open(sys.argv[1], 'wt') as my_file:
    data = "{0} {1}\n".format(len(matrix), len(matrix[0]))
    my_file.write(data)
    for row in matrix:
        line = ""
        for number in row:
            line += str(number) + " "
        my_file.write(line + "\n")