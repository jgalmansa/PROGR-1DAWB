
import math
import sys

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60


def duration_in_seconds(hours = 0, minutes = 0, seconds = 0):
    """Calcula la duración en segundos de un intervalo dado en horas, minutos y segundos.

    Args:
        hours: (int) número de horas
        minutes: (int) número de minutos
        seconds: (int) número de segundos

    Returns:
        total: Numero total de segundos
    """

    total = (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds

    return total


def convert_seconds_to_time(seconds):
    """Calcula la duración en horas, minutos y segundos de un intervalo dado en segundos

    Args:
        seconds: (int) número total de segundos

    Returns:
        Lista con los valores 
    """

    seconds = int(seconds)
    hours = int(seconds / SECONDS_PER_HOUR)
    minutes = int(seconds/SECONDS_PER_MINUTE - hours * SECONDS_PER_MINUTE) 
    last_seconds = int(math.fmod(seconds, SECONDS_PER_MINUTE))
    
    return (hours, minutes, last_seconds)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
num4 = int(sys.argv[4])

#print(num1, num2, num3, num4)

def max_product(num1,num2,num3,num4):
    '''Devuelve el mayor producto de dos de los numeros proporcionados como parámetros
    num1, num2, num3, num4: (int) Valores proporcionados para calcular el mayor producto de dos de ellos'''

    result = num1 * num2
    aux = num1 * num3
    if aux > result :
        result = aux
    
    aux = num1 * num4
    if aux > result :
        result = aux
    
    aux = num2 * num3
    if aux > result :
        result = aux
    
    aux = num2 * num4
    if aux > result :
        result = aux
    
    aux = num3 * num4
    if aux > result :
        result = aux

    return result
