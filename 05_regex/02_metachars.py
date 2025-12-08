###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

import os
os.system("clear")

import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, H0la de nuevo, H$la otra vez!"
pattern = "H.la"

found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No se ha encontrado el patrón")

text = "casa caasa cosa caza cisa cesa causa"
pattern = "c.sa"
matches = re.findall(pattern, text)

print(matches)

text = "Hola mundo, H0la de nuevo, H$la otra vez!"
pattern = r"H.la"

found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No se ha encontrado el patrón")

# Como utilizar la barra invertida para anular el significado especial de un metacaracter

text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)

print(f"Se encontraron {len(matches)} coincidencias")
print(matches)

# \d: coincide con cualquier dígito (0-9)

text = "El número de teléfono es 123456789"
matches = re.findall(r"\d{9}", text)

print(matches)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi número de teléfono es +34123456789, guardalo"
pattern = r"\+34\d{9}"
matches = re.search(pattern, text)

if matches:
    print(matches.group())

# \w: coincide con cualquier carácter alfanumérico (letras y números) y el guion bajo (_)
text = "el_rubius_69"
pattern = r"\w+"
matches = re.findall(pattern, text)
print(matches)

# \s: coincide con cualquier espacio en blanco (espacios, tabulaciones, saltos de línea)

text = "Hola mundo\n¿Cómo estas?\t"
pattern = r"\s"

matches = re.findall(pattern, text)
print(matches)

# ^: Coincide con el inicio de una cadena
text = "Hola mundo"
pattern = r"^\w" # validar el nombre de un usuario que debe empezar por letra
matches = re.search(pattern, text)

if matches:
    print("El nombre es válido")
else:
    print("El nombre no es válido")

phone = "+34123456789"
pattern = r"^\+\d{2,3}\d{9}$"
matches = re.search(pattern, phone)
if matches:
    print("El número de teléfono es válido")
else:
    print("El número de teléfono no es válido")

# $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"
matches = re.search(pattern, text)

if matches:
    print("El texto termina con 'mundo'")
else:
    print("El texto no termina con 'mundo'")

# EJERCICIO
# validar un correo electrónico

text = "guillefc@gmail.com"
pattern = r"^\w+@gmail.com$"

validador = re.search(pattern, text)
if validador:
    print("El correo es válido")
else:
    print("El correo no es válido")

# EJERCICIO
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extensión .txt
files = ["documento.txt", "imagen.png", "notas.txt", "video.mp4", "archivo.pdf"]


# \b: Coincide con el principio o final de una palabra
text = "casa casada casado casa"
pattern = r"\bcasa\b"

matches = re.findall(pattern, text)
print(matches)

# |: Coincidir con una opción u otra
text = "platano, manzana, aguacate, palta, pera"
pattern = r"aguacate|palta"

matches = re.findall(pattern, text)
print(matches)