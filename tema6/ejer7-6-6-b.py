"""Ejercicio 7.6.6. Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
k.
b) Devuelva una lista con aquellos que son múltiplos de k"""

"""Apartado B"""
def multiples_of_number(number_list, k):
    """
    Returns a list with the multiples of k

        number_list (list): a collection of integers
        k (int): a number to must be ultiple odd the result values

        Output (list): 
    """
    multiple_list = []
    for value in number_list:
        if (value % k == 0):
            multiple_list.append(value)

    return multiple_list


print(multiples_of_number([1, 4, 6, 2546, 4, 2565, 234, 68, 89, 134, 568, 345], 5))
print(multiples_of_number([1, 4, 6, 2546, 4, 2565, 234, 68, 89, 134, 568, 345], 2))

