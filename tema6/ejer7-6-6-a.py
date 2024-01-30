"""Ejercicio 7.6.6. Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
k.
b) Devuelva una lista con aquellos que son múltiplos de k"""


"""Apartado A"""
def classify_greater_less_equal_list(number_list, k):
    """
    Splits a list of numbers into three: those greater than a value, less than a value and equal to a value

        number_list (list): a collection of integers
        k (int): a number to split number_list by

        Output (list, list, list): 
    """
    greater_list = []
    less_list = []
    equal_list = []
    for value in number_list:
        if value < k:
            greater_list.append(value)
        elif value > k:
            less_list.append(value)
        else:
            equal_list.append(value)

    return greater_list, less_list, equal_list



print(classify_greater_less_equal_list([1, 4, 6, 2546, 4, 2567, 234, 68, 89, 134, 568, 345], 345))
print(classify_greater_less_equal_list([1,54,6,72,3,21,5,65,8,999,9,100], 10))


