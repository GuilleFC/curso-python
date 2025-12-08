import os
os.system("clear")

import re

# [: Coincide con cualquier carácter dentro de los corchetes

username = "rub.$ius_69+"
pattern = r"^[a\w._%+-]+$"

match = re.search(pattern, username)
if match:
    print(f"El nombre de usuario '{username}' es válido.", match.group())
else:
    print(f"El nombre de usuario '{username}' no es válido.", None)

# Buscar todas las vocales en una cadena
text = "Regular expressions are powerful!"
pattern = r"[aeiou]"
matches = re.findall(pattern, text, re.IGNORECASE)
print("Vocales encontradas:", set(matches))

# Una regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man fan ban pan tan can"
pattern = r"[mfb]an"
matches = re.findall(pattern, text)
print("Palabras encontradas:", matches)

# Ejercicio:
# Nos han complicado el asunto porque ahora hay palabras que encajan pero
# no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text)
print("Palabras encontradas con límites de palabra:", matches)

text = "22"
pattern = r"[0-9]"

matches = re.findall(pattern, text)
print("Dígitos encontrados entre 4 y 9:", matches)

r="[a-z"
r="[A-Za-z0-9]"

# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

# [^]: Coincide con cualquier carácter que NO esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print("Caracteres que no son vocales:", matches)