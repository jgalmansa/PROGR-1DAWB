"""Ejercicio 7.6.8. Inversión de listas
b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modifique la lista dada para invertirla, sin usar listas auxiliares.
"""
"""
Algorithm 
Input:
    my_list:list
Variables:
    aux: numeric
    i: numeric
    limit: numeric
Start:
    limit: len(my_list)/2
    for i between 0 and limit:
        aux <-- my_list[i]
        my_list[i] <-- my_list[size - i]
        my_list[size - i] <-- aux
Output: my_list

"""
def change_order_list(my_list):
    """
    Reverse the content of a list

        list (list): list to reverse
        Output (list): reversed list
    """
    
    size = int(len(my_list))
    limit = int(size / 2)
    for i in range(0, limit):
        aux = my_list[i]
        my_list[i] = my_list[size-i-1]
        my_list[size-i-1] = aux

    return my_list


def change_order_list_v2(my_list):
    """
    NO FUNCIONA
    Reverse the content of a list

        list (list): list to reverse
        Output (list): reversed list
    """
    
    length = int(len(my_list))
    for i in range(length):
        aux = my_list.pop()
        my_list.insert(0,aux)


    return my_list


print(change_order_list(['Di', 'buen', 'día', 'a', 'papa']))
print(change_order_list([7, 'Pepe', '3.8', True, 14, 'ttttt']))
print(change_order_list_v2(['Di', 'buen', 'día', 'a', 'papa']))
print(change_order_list_v2([7, 'Pepe', '3.8', True, 14, 'ttttt']))






'''
def change_order_list_mal(list):
    """
    Reverse the content of a list

        list (list): list to reverse
        Output (list): reversed list
    """
    list.reverse()
    return list
'''
