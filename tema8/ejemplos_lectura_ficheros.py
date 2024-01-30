import sys

#Ejemplo 1. Iterando en un bucle y leyendo linea a linea

"""
try:
    my_file = open(sys.argv[1])
except FileNotFoundError:
    print("The given file does no exist")
else: 
    for line in my_file:
        print(line)
    my_file.close()

"""

#Ejemplo 2. Leyendo el contendio de una vez. Meter en un try except como arriba

"""
my_file = open(sys.argv[1])
my_file_content = my_file.read()
print(my_file_content)
my_file.close()

"""

#Ejemplo 3. Datos binarios. Meter en un try except como arriba
"""
imgfile = open('Captura de pantalla 2023-10-30 171613.png', 'rb')
chunk_size = 1024
total_size = 0
data = imgfile.read(chunk_size)
total_size += len(data)

while data:
    data = imgfile.read(chunk_size)
    if data:
        total_size += len(data)
imgfile.close()
print("The size of the image is: ", total_size)

"""

#Ejemplo 4. Alternativa para datos binarios. Meter en un try except como arriba
"""
chunk_size = 1024
total_size = 0
with open('Captura de pantalla 2023-10-30 171613.png', 'rb') as imgfile:
    while True:
        data = imgfile.read(chunk_size)
        if not data:
            break
        total_size += len(data)
print("The total size of the image is: ", total_size)

"""

#Ejemplo 5. Alternativa 2 para datos binarios. Meter en un try except como arriba. Solo para archivos pequeños, lee todo del tirón

imgfile = open('C:/Users/1DAW-B/Documents/JuliaTmp/Captura de pantalla 2023-10-30 171613_movida.png', 'rb')
file_content = imgfile.read()
print('File size: ', len(file_content))
imgfile.close()