###
# 02 - booleanos()
# Los booleanos son un tipo de dato que puede tener dos valores: True o False
# Fundamental para el control de flujo y las condiciones
###

# Los booleanos representan valores de verdad: True (verdadero) y False (falso)

import os
os.system("cls")  # Limpiar la consola (Windows)

# print("\nValores booleanos básicos:")
print("True:", True)
print("False:", False)

# Operadores de comparación: devuelven un valor booleano.
# print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)     # True
print("5 < 3:", 5 < 3)     # False
print("5 == 5:", 5 == 5)   # True (igualdad)
print("5 != 3:", 5 != 3)   # True (desigualdad)
print("5 >= 5:", 5 >= 5)   # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)   # False (menor o igual que)

# print("\nComparación de Cadenas:")
print("manzana < pera", "manzana" < "pera")  # True (orden lexicográfico)
print("Banana == banana", "Banana" == "banana")  # False

# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)      # True
print("True and False:", True and False)    # False
print("True or False:", True or False)      # True
print("False or False:", False or False)    # False
print("not True:", not True)                # False
print("not False:", not False)              # True