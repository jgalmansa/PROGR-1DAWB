"""Ejercicio 7.6.8. Inversión de listas
a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di']."""

#Mi version
def change_order_list(my_list):
    """
    Reverse the content of a list

        my_list (list): given list to reverse
        Output (list): reversed list values
    """
    new_list = []
    n = len(my_list)
    for i in range(n):
        new_list.append(my_list[n-1])
        n -= 1
    
    return new_list



#Corregida en clase
def change_order_list_v2(my_list):
    """
    Reverse the content of a list

        my_list (list): given list to reverse
        Output (list): reversed list values
    """
    new_list = []
    for value in my_list:
        new_list.insert(0, value)
    
    return new_list

print(change_order_list(['Di', 'buen', 'día', 'a', 'papa']))
print(change_order_list_v2(['Di', 'buen', 'día', 'a', 'papa']))
print(change_order_list_v2([4, 'dfhs', 463, 'a', [True, 'asdf']]))