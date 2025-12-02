###
# 03 - castign de types
# Transformar un tipo de valor a otro
###

print("Conversión de tipos")
print(type(int("100")))

# print(2 + "100")

print(2 + int("100"))
print(str(2) + "100")

print(bool(0)) # solo se considera False el 0 cuando es numérico
print(bool(42))
print(bool("")) # solo se considera False la cadena vacía, si contiene un espacio ya es True
print(bool(-1))