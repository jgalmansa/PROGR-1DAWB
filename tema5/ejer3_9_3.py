'''Ejercicio 3.9.3. Escribir una función que, dados cuatro números, devuelva el mayor producto
de dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
más grande que se puede obtener entre ellos (8 = −2 × −4).'''

import sys

if len(sys.argv) != 5:
    print("The number of parameters is incorrect.")
    print("You need to enter 4 numbers.")
    exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
num4 = int(sys.argv[4])

#print(num1, num2, num3, num4)

def max_product(num1,num2,num3,num4):
    '''Devuelve el mayor producto de dos de los numeros proporcionados como parámetros
    num1, num2, num3, num4: (int) Valores proporcionados para calcular el mayor producto de dos de ellos'''

    result = num1 * num2
    aux = num1 * num3
    if aux > result :
        result = aux
    
    aux = num1 * num4
    if aux > result :
        result = aux
    
    aux = num2 * num3
    if aux > result :
        result = aux
    
    aux = num2 * num4
    if aux > result :
        result = aux
    
    aux = num3 * num4
    if aux > result :
        result = aux

    return result

print(max_product(num1,num2,num3,num4))

'''
Algorithm
max_product = null
for each number i from params:
    for each number j from params:
        if i != j:
            result <- i * j
            if result < max_product or max_product = null
                max_product <- result
'''
