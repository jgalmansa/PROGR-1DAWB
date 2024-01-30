"""Ejercicio 9.5.2. Diccionarios usados para contar.
a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}."""

def count_words(values):
    """
    Counts how many times a word appears on a string.

        values (string): text
    
        Output (dictionary): the key will be the word and the value will be how many times it was repeated
    """

    result = {}
    for word in values.split(" "):
        result[word] = values.count(word)

    return result

def count_words_v2(values):
    """
    Counts how many times a word appears on a string (case sensitive).

        values (str): text
    
        Output (dict): key -> word, value -> number of matches
    """

    times_by_word = {}
    word_list = values.split()
    for word in word_list:
        key = word.lower()
        if key not in times_by_word:
            times_by_word[key] = 1
        else:
            times_by_word[key] += 1

    return times_by_word

print(count_words("Que lindo día que hace hoy"))
print(count_words("Hola Don Pepito, Hola Don José Pepito"))

print(count_words_v2("Que lindo día que hace hoy"))
print(count_words_v2("Hola Don Pepito, hola Don José"))



