#Ejercicio 11.10.6. Persistencia de un diccionario
#   a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave y el segundo como diccionario.
#   b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo, y guarde el contenido del diccionario en el archivo, con el formato clave, valor.

import sys

if len(sys.argv) < 2:
    print("Syntax: ")
    print(sys.argv[0], " <file>")
    sys.exit()

SEPARADOR = ":"

def cargar_datos(filename):
    '''
    Loads a file with data that are converted into a distionary of keys and values
    filename (str): A text file with a collection of key and values separated by :
    Output (dict): get the file content as key-value pairs 
    '''
    file_as_dict = {}
    with open(filename) as myfile:
        for myline in myfile:
            data = myline.split(SEPARADOR)
            key = data[0]
            value = data[1].strip()
            file_as_dict[key] = value 

    return file_as_dict

print(cargar_datos(sys.argv[1]))