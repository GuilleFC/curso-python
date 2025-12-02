###
# 05 - input()
# La función input() permite al usuario ingresar datos durante la ejecución del programa
###

print("Hola, ¿Cómo te llamas?")
nombre = input()  # Espera a que el usuario ingrese un valor y presione Enter
print(f"¡Encantado de conocerte, {nombre}!")

age = input("¿Cuántos años tienes?\n")  # También se puede pasar un mensaje directamente a input()

print(f"¡Genial! Tienes {age} años.")
print(f"El año que viene tendrás {int(age) + 1} años.")  # Convertir la entrada a entero para hacer cálculos
# print(f"El año que viene tendrás {age + 1} años.")  # Esto concatenará '1' al string ingresado pero dará un error