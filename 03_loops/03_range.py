###
# 03 - range()
# Permite crear una secuencia de números, que es útil para iterar en bucles for cuando se necesita un contador.
###
import os
os.system("clear")

print("\nrange():")

# Generado una secuencia de números del 0 al 9
# for num in range(10):
#     print(num)

# range(inicio, fin)
# for num in range(5, 10):
#     print(num)

# range(inicio, fin, paso)
# for num in range(0, 1000, 5):
#     print(num)

# for num in range(-5, 0):
#     print(num)

# for num in range(10, 0, -1):
#     print(num)

# for num in range(0, 444):
#     print(num)

# Convertir un rango en una lista
nums = range(10)
list_of_numes = list(nums)
print(list_of_numes)

# sería para hacerlo 5 veces
contador = 0
while contador < 5:
    print("Hacer algo cinco veces")
    contador += 1

for _ in range(5):
    print("Hacer algo cinco veces")

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")