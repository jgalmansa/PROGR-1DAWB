"""Ejercicio 9.5.1. Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.
"""
#Incorrecta
def tuple_to_dict(tuple_list):
    """
    Convert a list of tuples to a dictionary, the first element will be the key and the second element the value

        tuple_list (list): list of tuples to convert

        Output (dict):  
    """

    result = {}
    for elem in tuple_list:
        result[elem[0]] = elem[1]
        #result.update({elem[0]:elem[1]})
    return result

#Correccion
def tuple_to_dict_v2(tuple_list):
    """
    Convert a list of tuples to a dictionary, the first element will be the key and the second element the value

        tuple_list (list): list of tuples to convert

        Output (dict):  
    """

    my_dict = {}
    for my_tuple in tuple_list:
        #my_tuple[0] #key
        #my_tuple[1:] #value
        key, *value = my_tuple
        if key not in my_dict:
            my_dict[str(key)] = value
        else:
            my_dict[str(key)].extend(value)


    return my_dict



print(tuple_to_dict([('Hola', 'don Pepito'), ('Hola', 'don Jose'),('Buenos', 'días')]))
print(tuple_to_dict([('Hola', 'don Pepito'), ('Adios', 'don Jose'),('Buenos', 'días')]))

print(tuple_to_dict_v2([('Hola', 'don Pepito'), ('Hola', 'don Jose'),('Buenos', 'días')]))
print(tuple_to_dict_v2([('Hola', 'don Pepito'), ('Adios', 'don Jose'),('Buenos', 'días', 'y adios')]))