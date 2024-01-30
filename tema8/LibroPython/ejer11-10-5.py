#Ejercicio 11.10.5. Escribir una función, llamada rot13, que reciba un archivo de texto de origen y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo caracter

"""#usar 
print(ord("a"))
print(chr(97))"""

import sys

if len(sys.argv) < 3:
    print("Syntax: ")
    print(sys.argv[0], " <origin_file> <final_file>")
    sys.exit()

LOWERCASE_A = "a"
LOWERCASE_Z = "z"
UPPERCASE_A = "A"
UPPERCASE_Z = "Z"
BASE_VALUE = 13
MOD_VALUE = 26

def is_letter(char):
    '''
    Checks if the character is a letter or not
    char (str): a single character
    Output (str): Boolean, True if its a letter, False otherwise
    '''
    """ Equivalentes:
    if char >= 'a' and char <= 'z':
        return True
    else:
        return False
        
    return char >= 'a' and char <= 'z'
    """
    is_lower_letter = char >= LOWERCASE_A and char <= LOWERCASE_Z
    is_upper_letter = char >= UPPERCASE_A and char <= UPPERCASE_Z

    return is_lower_letter or is_upper_letter


def encode_char(char):
    '''
    Transform the given character in another encoded.
    char (str): a single character
    Output (str): single encoded character
    '''
    if not is_letter(char):
        return char
    value = (ord(char) + BASE_VALUE) % MOD_VALUE
    value += ord(LOWERCASE_A) 
    if char >= LOWERCASE_A:
        value += ord(LOWERCASE_A) 
    else:
        ord(UPPERCASE_A)
    encoded_char = chr(value)
    return encoded_char


def encode_line(line):
    '''
    Transform the given line in another encoded.
    line (str): a sequence of characters endig in \n
    Output (str): encoded line
    '''
    encoded_line = ""
    for my_char in line:
        encoded_line += encode_char(my_char)
    return encoded_line


def rot13(origin_file, final_file):
    '''
    Encode the content of the original file into the final file
    origin_file (str): file to encode
    final_file (str): result of the codification
    '''
    try:
        o_file = open(origin_file)
        f_file = open(final_file, 'w')
    except FileNotFoundError:
        print("The file does not exist")
        sys.exit()
    else:
        for line in o_file:
            encoded_line = encode_line(line)
            f_file.write(encoded_line)
            
    o_file.close()
    f_file.close()


origin_file = sys.argv[1]
final_file = sys.argv[2]
print(rot13(origin_file, final_file))