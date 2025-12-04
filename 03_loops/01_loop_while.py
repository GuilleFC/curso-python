###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

import os
os.system('clear')

# print("\nBucle wile:")

# # Bucle con una simpel condición
# contador = 0
# while contador <= 5:
#     print(contador)
#     contador += 1 # Esto es fundamental para evitar un bucle infinito

# Utilizando la palabra break para romper el bucle
# print("\nBucle wile con break:")
# contador = 0

# while True:
#     print(contador)
#     contador += 1
#     if contador == 5:
#         break # Se sale del bucle

# Continue, que lo que hace es saltar esa iteración en concreto
# y continuar con el bucle
# print("\nBucle continue:")
# contador = 0

# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue
#     print(contador)

# else, esta condición cuando se ejecuta?
# print("\nBucle while con else:")
# contador = 0

# while contador < 5:
#     print(contador)
#     contador += 1
# else:
#     print('El Bucle ha terminado!')

# Pedirle al usuario un número que tiene que ser positivo sino, no le dejamos en paz
# numero = -1
# while numero < 0:
#     numero = int(input("Escribe un número positivo: "))
#     if numero < 0:
#         print("El número debe ser positivo. Intenta otra vez, majo o maja")

# print(f"El número que has introducido es {numero}")

numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un número positivo: "))
        if numero < 0:
            print("El número debe ser positivo. Intenta otra vez, majo o maja")
    except:
        print("Lo que has introducido no es un número, debes insertar un número para que el programa funcione")

print(f"El número que has introducido es {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")