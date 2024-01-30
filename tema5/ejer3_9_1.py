'''Ejercicio 3.9.1. Escribir dos funciones que permitan calcular:
a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
b) La duración en horas, minutos y segundos de un intervalo dado en segundos.'''

import math

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
        total: Lista con los valores 
    """

    seconds = int(seconds)
    hours = int(seconds / SECONDS_PER_HOUR)
    minutes = int(seconds/SECONDS_PER_MINUTE - hours * SECONDS_PER_MINUTE) 
    last_seconds = int(math.fmod(seconds, SECONDS_PER_MINUTE))
    
    return (hours, minutes, last_seconds)

print(duration_in_seconds(1, 4, 3), "segundos")
print(duration_in_seconds(0, 45, 0), "segundos")
print(duration_in_seconds(4, 30, 10), "segundos")
print(duration_in_seconds(minutes=4), "segundos")

print("Horas, minutos y segundos:")
print(convert_seconds_to_time(7578))
print(convert_seconds_to_time(3600))
print(convert_seconds_to_time(2000))