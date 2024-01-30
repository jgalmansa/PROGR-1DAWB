#Ejercicio que nos diga cual es la línea más larga y la más corta dentro de un fichero.

import sys

if len(sys.argv) < 2:
    print("Not enough arguments: Please write a valid text filename")
    sys.exit()

try:
    my_file = open(sys.argv[1])
except FileNotFoundError:
    print("The given file does no exist")
else:  
    longer = ''
    shorter = None
    for line in my_file:
        if shorter == None or len(line) < len(shorter):
            shorter = line
        if len(line) > len(longer):
            longer = line
    
    my_file.close()
    
    print("The longest line is: ", longer)
    print("The shortest line is: ", shorter)