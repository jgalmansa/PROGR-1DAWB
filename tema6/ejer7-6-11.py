"""Ejercicio 7.6.11. ⋆ Plegado de un texto. Escribir una función que reciba un texto y una longitud y devuelva una lista de cadenas de como máximo esa longitud. Las líneas deben ser cortadas correctamente en los espacios (sin cortar las palabras).
"""

"""
Algorithm cut_text
Input:
    my_text: text
    n: numeric
Variables:
    result: list
    left/start: numeric
    right/finish: numeric
    piece: text


Start:
    left <- 1
    right <- 10

    while right <= my_text_size:
        piece <- substring(my_text, left, right)
        while piece[rigth] != " " and piece[right + 1] != " ":
            right <- right - 1
            piece <- substr(piece, left, right)
        add piece to solution
        left = right
        right = left + 10



"""

def cut_text(my_text, size):
    """
    Cut the input text into pieces of given size without cuting words.

        my_text (str): provided text
        size (int): max length of each string

        Output (list): a collection of the pieces my_text is divided
    """

    left = 0
    right = size - 1
    solution = []
    total_length = len(my_text)

    while right < total_length - 1:
        piece = my_text[left:right + 1]
        while my_text[right] != " " and my_text[right + 1] != " ": 
            right -= 1
            piece = piece[left:right]
        solution.append(piece)
        left = right + 1
        right = min(left + size - 1, total_length - 1)
        
    return solution


example = "This is a very nice text with some statement"
n = 12
print(cut_text(example, n))

