# Julia Gadea Almansa García 02/11/2023

#Codifica el algortimo is_prime_number_v4 (en moodle - Algorithm solutions)

#Algoritmo:
'''
Algorithm is_prime_number_v4
Input:
    n: numeric
Variables:
    is_prime: boolean
    i: numeric
    result: numeric
    counter: numeric
    upper_limit: numeric
Start:
    counter <- 0
    if (mod(n, 2) = 0 and n != 2):    # checks if n is even
        counter <- 1
    else:
        upper_limit <- n/2
        for (i: 3..upper_limit, increasing=2) do:
            result <- mod(n, i)
            if (result = 0):
                counter <- counter + 1
    if (counter > 0):
        is_prime <- false
    else:
        is_prime <- true
Output:
    return is_prime
'''

#Codificación:
import math
from os import system
system("cls")

num = int(input("Enter a number to check if its prime: "))
counter = 0

if (math.fmod(num,2) == 0 and num != 2):
    counter = 1
else: 
    upper_limit = int(num / 2)
    for i in range(3, upper_limit, 2):
        result = math.fmod(num,i)
        if (result == 0):
            counter = counter + 1
            break #Afecta al for o al while más cercano

if (counter > 0):
    print ("The number is not prime")
else: 
    print ("The number is prime")







