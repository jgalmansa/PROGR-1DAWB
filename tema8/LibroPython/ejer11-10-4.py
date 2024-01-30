#Ejercicio 11.10.4. Escribir una función, llamada grep, que reciba una cadena y un archivo e imprima las líneas del archivo que contienen la cadena recibida.

import sys

if len(sys.argv) < 3:
    print("Syntax: ")
    print(sys.argv[0], " <filename> <string>")
    sys.exit()


def grep(filename, string):
    '''
    Print the lines in the file that contain the string provided
    filename (str): name of a existing text file  
    string (str): characters to search
    '''
    try:
        myfile = open(filename)
    except FileNotFoundError:
        print("The file does not exist")
        sys.exit()
    else:
        for line in myfile:
            if string in line:
                print(line)

    
    myfile.close()



myfile = sys.argv[1]
string = sys.argv[2]
print(grep(myfile, string))



