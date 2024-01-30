"""
Ejercicio 7.6.5. Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.
b) Devuelva la sumatoria y el promedio de los valores.
c) Devuelva una lista con el factorial de cada uno de esos números
"""
import math
from statistics import mean

"""a) Devuelva una lista con todos los que sean primos."""
def is_prime_number(num):
    """Points out whether a number is prime.
    num (int): given number
    Output (bool): True is num is prime, otherwise False
    """
    counter = 0

    if (math.fmod(num,2) == 0 and num != 2):
        counter = 1
    else: 
        upper_limit = int(num / 2)
        for i in range(3, upper_limit, 2):
            result = math.fmod(num,i)
            if (result == 0):
                counter = counter + 1
                break

    if (counter > 0):
        return False
    else: 
        return True



def check_prime(*args):
    """Checks if a list of numbers is prime
    args (int): list of numbers to check
    Output (int): list of only the prime numbers"""
    list_primes = []
    for num in args:
        result = is_prime_number(num)
        if result == True:
            list_primes.append(num)
    return list_primes



"""b) Devuelva la sumatoria y el promedio de los valores."""

def sum_and_avg(*args):
    """ Function that returns the sum of the given numbers, individualy and the average of them.
    args (list): numbers to use
    Output (int, float): first a list of each sum and then the average of the given numbers. 
    """

    suma = 0
    for num in args:
        suma += num
    counter = len(args)
    avg = suma / counter
    
    return (suma, avg)




def sum_and_avg_simple(*args):
    """ Function that returns the sum of the given numbers, individualy and the average of them.
    args (list): numbers to use
    Output (int, float): first a list of each sum and then the average of the given numbers. 
    """
    return (sum(args), mean(args))




"""c) Devuelva una lista con el factorial de cada uno de esos números"""

def factorial(*args):
    """ Function that calculates the factorial of each number provided
    args (list): collection of numbers 
    Output (int): factorial of each number
    """
    list_factorial = []
    for num in args:
        factorial = 1
        for i in range(1, num+1):
            factorial = factorial * i
        list_factorial.append(factorial)

    return list_factorial



def factorial_v2(value_list):
    """ Calculates the factorial of each number provided
    value_list (list): collection of numbers 
    Output (list): factorial of each number
    """
    list_factorial = []
    for num in value_list:
        result = math.factorial(num)
        list_factorial.append(result)

    return list_factorial







print("Apartado A: Numeros primos")
print(check_prime(1,2,3,4,5,6,7,8,9,10))

print("Apartado B: Suma y promedio ")
print(sum_and_avg(10,20))

print("Apartado B.2: Suma y promedio simplificado ")
print(sum_and_avg_simple(10,20))

print("Apartado C: Factorial ")
print(factorial(3,4))

print("Apartado C: Factorial corregido")
print(factorial_v2([2,4,6,9]))