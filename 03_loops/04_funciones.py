###
# 04 - Funciones
# Bloques de código reutilizables que realizan tareas específicas
###

""" Definición de una función
def nombre_de_la_funcion(parametro1, parametro2, ...):
    # docstring opcional
    # cuerpo de la función
    return valor_de_retorno # Opcional
"""
import os
os.system('clear')

# Ejemplo de funcón para imprimir algo en consola
# def saludar():
#     print("Hola!")

# saludar()

# # Ejemplo de funcón con parámetro
# def saludar_a(nombre):
#     print(f"Hola, {nombre}!")

# saludar_a("Guillermo")

# # El parámetro es lo que acepta la función, el argumento es lo que se le pasa a la función al momento de llamarla

# def sumar(a, b):
#     suma = a + b
#     return suma

# result = sumar(3, 5)
# print(result)

# # Documentar las funciones con docstrings
# def restar(a, b):
#     """Resta dos números y devuelve el resultado"""
#     return a - b

# print(restar(10,5))

# Parámetros por defecto
# def multiplicar(a, b=2):
#     return a * b

# print(multiplicar(4))    # Usa el valor por defecto de b
# print(multiplicar(4,3)) # Sobrescribe el valor por defecto de b

# Argumentos por clave
def describir_persona(nombre,edad,genero):
    print(f"Soy {nombre}, tengo {edad} años y soy {genero}")

describir_persona("Ana",28,"mujer")

# Argumentos por clave (keyword arguments)
# Parámetros nombrados al llamar a la función
def describir_persona_a(nombre,edad,genero):
    print(f"Soy {nombre}, tengo {edad} años y soy {genero}")

describir_persona_a(genero="hombre", edad=32, nombre="William")

# Argumentos de longitud variable (*args)
def sumar_numeros(*args):
    total = 0
    for num in args:
        total += num
    print(total)

sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Argumentos de clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="Laura", edad=25, ciudad="Madrid")
mostrar_informacion_de(profesion="Ingeniera", empresa="TechCorp")
mostrar_informacion_de()  # Llamada sin argumentos

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora