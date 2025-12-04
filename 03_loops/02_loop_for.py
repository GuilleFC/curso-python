###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

import os
os.system("clear")

print("\nBucle for:")

# Iterar una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("frutas: ", fruta)

# Iterar sobre cualquier cosa que sea iterable
nombre = "Guillermo"
for letra in nombre:
    print("Letra :", letra)

# enumerate: obtener el índice y el valor
print("\nUsando enumerate:")
frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(frutas): # Tener siempre en cuenta el orden de los valores retornados, el primero es el índice y el segundo el valor
    print(f"Índice: {indice}, Fruta: {fruta}")

# Bucles anidados
print("\nBucle for anidado:")
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# break
print("\nUso de break:")
animales = ["perro", "gato", "pez", "pájaro"]
for indice, animal in enumerate(animales):
    if animal == "gato":
        print(f"¡Encontramos el animal misterioso, el {animal} y está escondido en la posición {indice}!")
        break

# continue
print("\nUso de continue:")
animales = ["perro", "gato", "pez", "pájaro"]
for animal in animales:
    if animal == "pez":
        print(f"Vamos a ignorar al {animal} porque este no tiene patas")
        continue
    print(animal)

# comprensión de listas (list comprehension)
print("\nList comprehension:")
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero ** 2 for numero in numeros]
print(cuadrados)

### Muestra los números pares de una lista usando list comprehension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")