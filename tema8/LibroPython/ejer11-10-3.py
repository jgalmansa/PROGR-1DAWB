#Ejercicio 11.10.3. Escribir una función, llamada wc, que dado un archivo de texto, lo procese e imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el archivo.


import sys

if len(sys.argv) < 2:
    print("Syntax: ")
    print(sys.argv[0], " <file>")
    sys.exit()


def wc(filename):
    '''
    Print the number of lines, words and characters of a text file.
    filename (str): name of a existing text file    
    '''
    try:
        myfile = open(filename)
    except FileNotFoundError:
        print("The file does not exist")
        sys.exit()
    else:
        lines = 0
        words = 0
        characters = 0
        for i in myfile:
           lines += 1 
           words += len(i.split())
           characters += len(i)
        print("Lines:",lines)
        print("Words:", words)
        print("Characters:", characters)

    
    myfile.close()



myfile = sys.argv[1]
print(wc(myfile))









