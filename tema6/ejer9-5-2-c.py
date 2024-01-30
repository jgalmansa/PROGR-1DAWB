"""Ejercicio 9.5.2. Diccionarios usados para contar.
c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados.
Nota: utilizar el módulo random para obtener tiradas aleatorias.
"""

from random import randint

def count_value_dice_v2(rolls):
    """
    Count the result of thowing two dices.

        rolls (int): number of rolls for the dices

        Output (dict): key -> result of the throw, value -> number of repetitions.
    """

    number_by_result = {}
    for i in range(rolls):
        result = str(randint(2,12))
        if result in number_by_result:
            number_by_result[result] += 1
        else:
            number_by_result[result] = 1

    return number_by_result

print(count_value_dice_v2(100))







def count_value_dice(rolls):
    """
    Count how many times a dice value appears with 2 dices

        rolls (int): number of rolls for the dices

        Output (dictionary): count of the values

    """
    dice1 = []
    dice2 = []
    for i in range(rolls):
        dice1.append(randint(1,6))
        dice2.append(randint(1,6))
        result = {}
        for num in dice1:
            result[num] = dice1.count(num)
        for num in dice2:
            result[num] = dice1.count(num)

    return result

#print(count_value_dice(10))



