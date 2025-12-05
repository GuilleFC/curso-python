##
# 01 - Expresiones regulares
# 

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""
import os
os.system("clear")

# 1. Importar el módulo re
import re
# 2. Crear un patrón, que es una cadena de texto que define lo que queremos encontrar
pattern = "Hola"
# 3. Crear una cadena de texto donde buscaremos el patrón
text = "Hola mundo"
# 4. Usar re.search() para buscar el patrón en la cadena de texto
resultado = re.search(pattern, text)

if resultado:
    print("¡Patrón encontrado!")
else:
    print("Patrón no encontrado.")

# .group(): Devuelve la cadena que coincide con el pattern
print(resultado.group())  # Salida: Hola

# .start(): Devuelve el índice de inicio de la coincidencia
print(resultado.start())  # Salida: 0

# .end(): Devuelve el índice de fin de la coincidencia
print(resultado.end())    # Salida: 4

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)

if found_ia:
    print(f"He encontrado el patron en el texto en la posición {found_ia.start()} y termina en la posición {found_ia.end()}")
else:
    print("Patrón no encontrado")

# -------------------------

### Encontrar todas las coincidencias de un patrón
# .findall(): devuelve una lista con todas las coincidencias del patrón en la cadena de texto
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"
matches = re.findall(pattern, text)
print(matches)

# ------------------------

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

# Modificadores

# Los modificadores con opciones que se pueden agregar a un patron para cambiar su comportamiento.

# re.IGNORECASE o re.I: Hace que la búsqueda no distinga entre mayúsculas y minúsculas.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala como dicen. Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)

if found:
    print(found)

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"

### Reemplazar el texto

# .sub() reemplaza todas las coincidencias de un patrón en un texto

text = "Hola mundo! Hola de nuevo!"
pattern = "Hola"
replacement = "Adiós"
new_text = re.sub(pattern, replacement, text)
print(new_text)