#Ejercicio 11.10.1. Escribir una función, llamada head que reciba un archivo y un número N e imprima las primeras N líneas del archivo.

import sys

if len(sys.argv) < 3:
    print("Syntax: ")
    print(sys.argv[0], " <file> <number of lines>")
    sys.exit()


def head(filename, n):
    '''
    Prints the first n lines of the provided file.
    n (int): lines to show
    filename (str): file provided
    '''
    try:
        myfile = open(filename)
    except FileNotFoundError:
        print("The file does not exist")
        sys.exit()
    else:
        for i in range(int(n)):
            line = myfile.readline()
            print(line)
        myfile.close()



myfile = sys.argv[1]
n = sys.argv[2]
print(head(myfile,n))