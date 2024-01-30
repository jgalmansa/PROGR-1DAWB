"""Ejercicio 7.6.7. Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el nombre, luego la inicial con un punto, y luego el apellido."""

def build_full_names (tuple_list):
    """
    Returns a collection of names (firt name, initial second name, lastname)

        tuple_list (list): collection of tuples with firt name, initial second name and lastname

        output(list): collection of names as string
    """

    full_name = [tuple_list[1] + " " + tuple_list[2] + ". " + tuple_list [0]]
    

    return full_name


print(build_full_names(["Smith", "John", "S"]))


#Completar
def build_full_names_v2 (tuple_list):
    """
    Returns a collection of names (firt name, initial second name, lastname)

        tuple_list (list): collection of tuples with firt name, initial second name and lastname

        output(list): collection of names as string
    """
    value_list = []
    for value in tuple_list:
        value_list.append(value[1] + " " + value[2] + ". " + value [0])

    return value_list


print(build_full_names_v2([("Smith", "John", "Ms"),("apellido", "nombre", "letra")]))