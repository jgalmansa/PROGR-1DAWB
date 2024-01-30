#Ejemplo 1. 
"""
lines = ['One', 'Two', 'Three', 1, 2, 3.5, True, False, 'aaa']
lines2 = ['Four\n', 'Five\n', 'Six\n']
myfile = open('myfile.txt', 'w')
for line in lines:
    myfile.write(str(line) + '\n')
myfile.writelines(lines2)
myfile.close()

"""

#Ejemplo 2. Pidiendo el contendio del fichero al usuario. 
"""
import sys

myfile = open(sys.argv[1], 'a')

while True:
    typedtext = input("Type text: ")
    if typedtext == '0':
        break
    myfile.write(typedtext + '\n')

myfile.close()

"""

#Ejemplo 3. Conversion binaria/texto
"""
import pickle

data_list = [1, 2.5, 'Three', False]
print("Original: ", data_list)

bytelist = pickle.dumps(data_list)
print("Converted to bytes: ", bytelist)

original_data = pickle.loads(bytelist)
print("Back to original: ", original_data)
"""

#Ejemplo 4. Escribir un archivo binario 
"""
import pickle

data_dict = {'Brand': 'Porsche', 'Model': '911'}

with open('myfile.bin', 'ab') as myfile:
    data = pickle.dumps(data_dict)
    myfile.write(data)
"""

#Ejemplo 5.  Lee un fichero binario y muestra el contenido en modo texto

import pickle

with open('myfile.bin', 'rb') as myfile:
    data = myfile.read()
    orig_data = pickle.loads(data)
    print(orig_data)
