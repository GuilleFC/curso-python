###
# 04 - Variables
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinámico y de tipado fuerte
###

# Asignar una variable
# solo con el símbolo =
# mensaje = "Hola, Mundo!"
# print(mensaje)

# age = 25
# print(age)

# age = 32
# print(age)

# Tipado dinámico = el tipo de dato lo asigna el valor
# o sea que, se determina automáticamente

age = 25
print(type(age))

age = "32"
print(type(age))

# Cadenas literales formateadas (f-strings)
print(f"Tengo {age} años")

# Convenciones de nombres de variables
my_variable = 10  # snake_case
myVariable = 20   # camelCase -> no se utiliza en Python habitualmente

MI_CONSTATE = 3.14 # UPPER_CASE -> para constantes (valores que no cambian)

# Palabras reversadas (keywords) no se pueden usar como nombres de variables
# print = "Hola"  # Esto daría un error porque print es una palabra reservada