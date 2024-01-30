#Ejercicio 11.10.6. Persistencia de un diccionario
#   a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave y el segundo como diccionario.
#   b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo, y guarde el contenido del diccionario en el archivo, con el formato clave, valor.

import sys

if len(sys.argv) < 2:
    print("Syntax: ")
    print(sys.argv[0], " <file>")
    sys.exit()

SEPARADOR = ":"

def guardar_datos(mydict, filename):
    '''
    Saves the content of a given dictionary into a text file
    mydict (dict): dictionary of keys and values 
    filename (str): destination file to save teh data of the dictionary 
    '''

    with open(filename, "w") as myfile:
        for key in mydict:
            value = str(mydict[key])
            line = key + SEPARADOR + value + "\n"
            myfile.write(line)


paises = {
    'Spain': 'Madrid', 
    'France': 'Paris', 
    'Portugal': 'Lisbon', 
    'Germany': 'Berlin', 
    'Australia': 'Canberra', 
    'United Stated': 'Washinton DC', 'Canada': 'Ottawa', 
    'Argentina': 'Buenos Aires'}

print(guardar_datos(paises, sys.argv[1]))