
import sys
from pickle import loads

if len(sys.argv) < 2:
    print("Syntax: ")
    print(sys.argv[0], " <file>")
    sys.exit()


def cargar_datos(filename):
    '''
    Loads a file with data that are converted into a distionary of keys and values
    filename (str): A text file with a collection of key and values separated by :
    Output (dict): get the file content as key-value pairs 
    '''
    mydict = None
    with open(filename, 'rb') as myfile:
        encoded_data = myfile.read()
        mydict = loads(encoded_data)

    return mydict

print(cargar_datos(sys.argv[1]))