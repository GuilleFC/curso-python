###
# 01 - Sentencias condicionales (if, elif, else)
# Las sentencias condicionales permiten ejecutar diferentes bloques de código
###

import os
os.system("cls")  # Limpiar la consola (Windows)

# print("\n Sentencia simple condicional")

# edad = 32
# if edad >= 18:
#     print("Eres mayor de edad")
#     print("Felicidades!")

# edad = 15
# if edad >= 18:
#     print("Eres mayor de edad")
#     print("Felicidades!")

# print("\n Sentencia simple condicional con else")

# edad = 32
# if edad >= 18:
#     print("Eres mayor de edad")
# else:
#     print("Eres menor de edad")

# print("\n Sentencia simple condicional con elif")

# nota = 7
# if nota >= 9:
#     print("Sobresaliente")
# elif nota >= 7:
#     print("Notable")
# elif nota >= 5:
#     print("Aprobado")
# else:
#     print("Suspenso") 

print("\nSentencia condicional doble con operadores lógicos")
edad = 20
tiene_licencia = False

# if edad >= 18 and tiene_licencia:
#     print("Puedes conducir")
# else:
#     print("No puedes conducir!")

# Estas viviendo en Paraguay
# if edad >= 18 or tiene_licencia:
#     print("Puedes conducir")
# else:
#     print("Paga el policía y te dejará conducir")

# print("\nSentencia condicional anidada")
# edad = 20
# tiene_dinero = True

# if edad >= 18:
#     if tiene_dinero:
#         print("Puedes entrar a la discoteca")
#     else:
#         print("No tienes dinero para entrar")
# else:
#     print("Eres menor de edad, no puedes entrar")

# numero = 5
# if numero: # True
#     print("El número es diferente de cero")

# numero = 0
# if not numero: # False
#     print("El número es cero")

# numero = 3 # asignación
# es_el_tres = (numero == 3) # comparación
# if es_el_tres:
#     print("El número es tres")

print("\nLa condición ternaria:")
# es una forma concisa de un if-else para asignar valores o ejecutar expresiones basadas en una condición.
# [código si cumple la condición] if [condición] else [código si no cumple la condición]

edad = 14
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)