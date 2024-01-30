"""
Ejercicio 7.6.9. Escribir una función empaquetar para una lista, donde epaquetar significa indicar la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones).
Por ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5,
1), (1, 2), (3, 2)].
"""

def wrap(values):
    """
    Count how many consecutive times a number appears 

        values (list): collection of values

        Output (list): collection of tuples, values and repetitions
    """
    previous = None
    result = []
    counter = None
    for elem in values:
        if previous == elem:
            counter += 1
        else:
            my_tuple = (previous, counter)
            if previous != None:
                result.append(my_tuple)
            counter = 1

        previous = elem
    my_tuple = (previous, counter)
    result.append(my_tuple)

    return result
        
print(wrap([1, 1, 1, 3, 5, 1, 1, 3, 3, 9]))
