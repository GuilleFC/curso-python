###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

import os
os.system('clear')

# ejemplo tipico de diccionario
persona = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}

# Para acceder a los valores del diccionario usamos las claves
print(persona["nombre"])
print(persona["calificaciones"])
print(persona["socials"]["twitter"])

# cambiar valores al acceder
persona["nombre"] = "Guillermo"
print(persona["nombre"])

del persona["edad"]
print(persona)

es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")

# Sobreecribir un diccionario con otro diccionario
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

a.update(b)
print(a)

# comprobar si una clave existe en un diccionario
print("nombre" in persona)
print("name" in persona)

# obtener todas las claves
print("\nkeys:")
print(persona.keys())

# obtener todos los valores
print("\nvalues:")
print(persona.values())

# obtener todos los pares clave-valor
print("\nitems:")
print(persona.items())