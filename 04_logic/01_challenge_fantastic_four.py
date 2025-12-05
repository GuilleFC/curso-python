"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es fundamental para enfrentar cualquier desafío. En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. Esta función debe contar cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la mente y el fuego está en equilibrio y la función debe retornar True.
- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""
import os
os.system('clear')

def check_is_balanced(text):
    text = text.upper()  # Convertir el texto a mayúsculas para contar sin distinción de caso
    # contar facilmente el número de veces que aparece cada letra
    count_r = text.count('R')
    count_j = text.count('J')

    return count_r == count_j
    
    # if count_r == count_j:
    #     print(f"Cantidad de R: {count_r}, Cantidad de J: {count_j}, son cantidades iguales")
    #     return True
    # else:
    #     print(f"Cantidad de R: {count_r}, Cantidad de J: {count_j}, no son cantidades iguales")
    #     return False
    
print(check_is_balanced("Reed Richards y Johnny Storm son parte de los 4 Fantásticos"))  # False
print(check_is_balanced("RRJJ"))  # True