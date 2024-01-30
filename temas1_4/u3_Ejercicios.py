# Julia Gadea Almansa García 1º WEB B
# Unidad 3: Control de flujo - Ejercicios

# Primera tanda: Hacer ejercicios 1-2-3 19/10/2023

#Importación de librerías
import math
import random
from os import system

#------------------------------------------------------------#
#Menu
system("cls")

print('Menu de ejercicios del tema 3:')
print(' 1. Par o impar')
print(' 2. Saber el ultimo digito de un numero')
print(' 3. Representar un numero en binario')
print(' 4. Mostrar todos los numero pares entre los dos numeros que digas')
print(' 5. Calcular todos los divisores de un numero')
print(' 6. Calcular el maximo comun divisor')
print(' 7. Calcular el minimo comun multiplo (de mi forma)')
print(' 7b. Calcular el minimo comun multiplo (con while, forma del profesor)')
print(' 7c. Calcular el minimo comun multiplo (con for pero interrumpiendo la ejecucion, forma del profesor)')
print(' 8. Resolver la formula de la sumatoria')
print(' 9. Adivinar un numero')
print(' 10. Dibujar un cuadrado')
ejer = input("Elija el ejercicio a ejecutar (1-10): ")


if (ejer == '1'):
    system("cls")
# 1. Write a program to point out whether a number that a user provides is odd or even.
    #Algorithm is_even_number
    #Input:
    num = input ("Please enter a number to check if its even: ")

    #Variables Start y Output:
    is_even = None
    result = math.fmod(int(num), 2)

    if result == 0:
        is_even = True
    else:
        is_even = False


    print (is_even)


#------------------------------------------------------------#

#Menu

elif (ejer == '2'):
    system("cls")
# 2. Write a program that, given an integer number, returns the digit of the units. For instance, for 153 you should return 3.
    # Algorithm return_unit_digit
    # Input 
    num = input("Please enter a number: ")
    num = int(num)
    # Variables Start and Output
    last_digit = math.fmod(num, 10)

    print("The last digit is " + str(last_digit))


#------------------------------------------------------------#

#Menu

elif (ejer == '3'):
    system("cls")
# 3. Write a program that takes a number from the user input and represents that number with binary digits (do not use direct conversion from the language). Do the same thing with octal and hexadecimal conversions.

    # Algorithm converion_to_binary_octal_hexadecimal
    # Input 
    num = input("Please enter a decimal number: ")
    num = int(num)
    # Variables Start and Output
    resultBin = ''

    while (num > 0):
        rest = math.trunc(math.fmod(num,2))
        resultBin = str(rest) + resultBin
        num = int(num/2)


    print("In binary is: ", resultBin)
    print(bin(25))
    


#------------------------------------------------------------#

#Menu

elif (ejer == '4'):
    system("cls")
# 4. Write a program to show all the even numbers between two numbers that a user provides as an input.
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    result = ''

    if num1 < num2:
        low = num1
        top = num2
    else: 
        low = num2
        top = num1 
        
    remainder = math.fmod(int(low), 2)
    for i in range(low,top + 1, 2):
        #print ('resto: ', remainer)
        if (remainder != 0):
            i = int(i) +1
        result = result + str(i) + ' '
        #print (i)
    print ('All the even numbers between them are: ' + result)




#------------------------------------------------------------#

#Menu

elif (ejer == '5'):
    system("cls")
# 5. Write a program to calculate all the divisors of a number that a user provides as an input.
    num = int(input("Please enter a number to calculate its divisors: "))
    result = ''
    for i in range(1, int(num/2)+1):
        remainder = math.fmod(num, i)
        if (remainder == 0):
            result = result + str(i) + ' '
    print ('All the divisors of the number are: ' + result)




#------------------------------------------------------------#

#Menu

elif (ejer == '6'):
    system("cls")
# 6. Write a program to calculate the greatest common divisors of two numbers that a user provides as an input.
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    
    greatest_common_divisor = ''
    
    '''
    if (num1 > num2):
        limit = num2
    else:
        limit = num1
    '''

    limit = min(num1,num2)    # En vez del if para comparar y saber cual es menor
        
    for i in range(1, limit+1):
        if (math.fmod(num1, i) == 0 and math.fmod(num2, i) == 0):
            greatest_common_divisor = i
    print ('The greatest common divisor of the two numbers is ', greatest_common_divisor)




#------------------------------------------------------------#

#Menu

elif (ejer == '7'):
    system("cls")
# 7. Write a program to calculate the minimum common multiple of two numbers that a user provides as an input.
#No es la forma más recomandable, necesita demasiados cálculos 
    print ('Mi forma de hacer el ejercicio')
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    
    minimum_common_multiple = ''

    low_limit = max(num1,num2)
    top_limit = num1 * num2 + 1

    for i in range(top_limit, low_limit-1, -1):
        #print('for', i)
        if ( math.fmod(i,num1) == 0 and math.fmod(i,num2) == 0 ):
            minimum_common_multiple = i
            #print('if', i)
    print ('The minimun common multiple is', minimum_common_multiple)

#------------------------------------------------------------#

elif (ejer == '7b'):
#Tampoco muy recomendable, es largo y requiere más calculos
    system("cls")
    print ('Forma 1 del profesor, usando while')
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    
    start = max(num1, num2)
    end = num1 * num2 
    is_Found = False
    i = start

    while not is_Found and i <= end:
        remainder1 = math.fmod(i, num1)
        remainder2 = math.fmod(i, num2)
        is_Found = remainder1 == 0 and remainder2 == 0

        if is_Found:
            is_Found = True
            mcm = i
        i = i + 1
    
    print ('The minimun common multiple is', mcm)



#------------------------------------------------------------#

elif (ejer == '7c'):
#Forma más eficiente, corta i entendible
    system("cls")
    print ('Forma 2 del profesor, usando for e interrumpiendo el bucle')
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    start = max(num1, num2)
    end = num1 * num2 

    mcm = None
    for i in range(start, end+1):
        remainder1 = math.fmod(i, num1)
        remainder2 = math.fmod(i, num2)
        if (remainder1 == 0 and remainder2 == 0):
            mcm = i
            print ('The minimun common multiple is', mcm)
            break



#------------------------------------------------------------#

#Menu

elif (ejer == '8'):
    system("cls")
# 8. Write a program to calculate the value of the following formula, provided the number n as an input: ∑(j=1..n) ∑(i=1..j) j · i2
    n = int(input('Provide a number to calculate the summation: '))
    result = 0

    for j in range(1,n+1): #Importante +1 en los dos bucles!!
        for i in range(1,j+1):
            result = result + (j * pow(i,2))

    print ('The result is:',result)
        


#------------------------------------------------------------#

#Menu

elif (ejer == '9'):
    system("cls")
# 9. Write a program to guess a number. To do this, ask for a number N, and then ask for numbers pointing out either “greater” or “lesser” (depending on whether the given number it is greater or not as regards to N). The process ends when the user gets it right.

    num = int(input("Lets guess a number between 0 and 100, enter your guess: "))
    correct = random.randint(0,100) 

    while num >= 0 and num <= 100:
        if num > correct:
            print ("Greater than the correct number")
            num = int(input("Try again: "))
        elif num < correct:
            print ("Lesser than the correct number")
            num = int(input("Try again: "))
        elif num == correct:
            print("Correct!")
            break



#------------------------------------------------------------#

#Menu

elif (ejer == '10'):
    system("cls")
# 10. Write a program to draw a square of n elements on each side using *.
    n = int(input('Please enter a number to determinate the elements of the square: '))

    print('--------------')

    #Forma 1 con relleno
    for i in range(1,n+1):
        print('* '*n)
    
    print('--------------')

    #Forma 2 sin relleno
    print ('* '*n)
    for i in range(1,n-1):
        print ('*','  ' *int(n-2),'*')
    print ('* '*n)

    print('--------------')

    #Forma 3 del profesor
    for i in range(1, n+1): #rows
        line = ''
        for j in range(1, n+1): #colums
            if j == 1 or j == n or i == 1 or i == n:
                line = line + '* '
            else: 
                line = line + '  '
        print(line)


#------------------------------------------------------------#

else:
    print("Introduzca un número válido")
