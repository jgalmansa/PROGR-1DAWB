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

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    print("The file does not exist")
    sys.exit()
else:
    file.close()
    with open(sys.argv[1], 'rt') as my_file:
        lines = my_file.readlines() #lines -> list of string
        matrix = [] #matrix -> list od list (2 levels)
        values = lines[0].split()
        num_rows = int(values[0])
        num_cols = int(values[1])
        
        for line in lines[1:]:
            values = line.split()
            int_values= []
            
            for value in values:
                int_values.append(int(value))
            matrix.append(int_values)

        if len(lines[1:]) != num_rows:
            print("error lines", lines[1:])
            print("error rows", num_rows)
        elif len(int_values) != num_cols:
            print("error values", int_values)
            print("error cols", num_cols)
        else:
            print("Number of rows:", num_rows)
            print("Number of columns:", num_cols)
            print("matrix values:", matrix)





