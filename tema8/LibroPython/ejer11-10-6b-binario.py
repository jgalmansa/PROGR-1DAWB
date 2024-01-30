
import sys, pickle

if len(sys.argv) < 2:
    print("Syntax: ")
    print(sys.argv[0], " <file>")
    sys.exit()


def guardar_datos_binarios(mydict, filename):
    '''
    Saves the content of a given dictionary into a text file
    mydict (dict): dictionary of keys and values 
    filename (str): destination file to save teh data of the dictionary 
    '''

    myfile = open(filename, 'wb')
    data = pickle.dumps(mydict)
    myfile.write(data)
    myfile.close()


paises = {
    'Spain': 'Madrid', 
    'France': 'Paris', 
    'Portugal': 'Lisbon', 
    'Germany': 'Berlin', 
    'Australia': 'Canberra', 
    'United Stated': 'Washinton DC', 'Canada': 'Ottawa', 
    'Argentina': 'Buenos Aires'}

print(guardar_datos_binarios(paises, sys.argv[1]))