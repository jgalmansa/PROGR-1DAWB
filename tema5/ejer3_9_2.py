"""
Ejercicio 3.9.2. Usando las funciones del ejercicio anterior, 
escribir un programa que pida al usuario dos intervalos expresados
en horas, minutos y segundos, sume sus duraciones, y muestre por 
pantalla la duración total en horas, minutos y segundos.
"""

from funcionesT5 import duration_in_seconds, convert_seconds_to_time
import sys

#Para sustituir los input usamos sys.argv[]
"""
print("Introduzca dos intervalos expresados en horas, minutos y segundos:")
print("Primer intervalo")
hours1 = int(input("Horas: "))
minutes1 = int(input("Minutos: "))
seconds1 = int(input("Segundos: "))

print("Segundo intervalo")
hours2 = int(input("Horas: "))
minutes2 = int(input("Minutos: "))
seconds2 = int(input("Segundos: "))
"""

if len(sys.argv) < 7:
    print("The number of parameters is incorrect")
    exit()

hours1 = int(sys.argv[1])
minutes1 = int(sys.argv[2])
seconds1 = int(sys.argv[3])
hours2 = int(sys.argv[4])
minutes2 = int(sys.argv[5])
seconds2 = int(sys.argv[6])

duracion1 = duration_in_seconds(hours1, minutes1, seconds1)
duracion2 = duration_in_seconds(hours2, minutes2, seconds2)

suma = int(duracion1 + duracion2)

horas_total, minutos_total, segundos_total = convert_seconds_to_time(suma)


print(str(horas_total), "horas", str(minutos_total), "minutos", str(segundos_total), "segundos")
