###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import os
os.system('clear')

import re

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 1:
# ¿Cuántas palabras tienen de 0 a más "a" y después una "b"?

# +: Una o más veces
text = "dddd aaa ccc a bb aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

# ?: Cero o una vez
text = "aaaba"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 600 123 456"
pattern = r"(\+|00)?34 \d{3} \d{3} \d{3}"
match = re.findall(pattern, phone)
print(match)

# {n}: Exactamente n veces
text = "aaaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
print(matches)

# {m,n}: De m a n veces
text = "u uu uuu uuuu"
pattern = "u{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: Encuentra las palabras que tienen más de 4 letras
palabra = "ala casa árbol león cinco murciélago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, palabra)
print(matches)

palabra = "ala fantástico casa árbol león cinco murciélago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, palabra)
print(matches)