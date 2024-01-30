"""Ejercicio 9.5.2. Diccionarios usados para contar.
b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, y los devuelva en un diccionario"""

def count_caracters_V2(values):
    """
    Counts how many times a caracter appears on a string.

        values (str): text
    
        Output (dict): key -> caracter, value -> how many times it was repeated
    """

    number_by_char = {}
    for char in values:
        key_char = char.lower()
        if key_char not in number_by_char:
            number_by_char[key_char] = 1
        else:
            number_by_char[key_char] += 1
            
    return number_by_char

print(count_caracters_V2("Que lindo día que hace hoy"))
print(count_caracters_V2("aHfFj ADWAn 3J7_:"))








def count_caracters(values):
    """
    Counts how many times a caracter appears on a string.

        values (string): text
    
        Output (dictionary): the key will be the caracter and the value will be how many times it was repeated
    """

    caracter_by_string = {}
    for word in values:
        caracter_by_string[word] = values.count(word)

    return caracter_by_string

#print(count_caracters("Que lindo día que hace hoy"))
#print(count_caracters("aHfj ADWAn asJh"))





