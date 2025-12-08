# Trabajando con fechas y horas en Python

import os
os.system("clear")

from datetime import datetime, timedelta
import locale

# Establecer la configuración regional a español (España)
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
# 1. Obtener la fecha y hora actual
now = datetime.now()
print("Fecha y hora actual:", now)

# 2. Crear una fecha y hora específica
specific_date = datetime(2023, 12, 25, 10, 30)
print("Fecha y hora específica:", specific_date)

# 3. Formatear fechas y horas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato deseado
# formatted_date = now.strftime("%d/%m/%y %H:%M:%S")
# print("Fecha formateada:", formatted_date)

formatted_date = now.strftime("%A %B %Y %H:%M:%S")
print("Fecha formateada:", formatted_date)

# 4. Operaciones con fechas (sumar, restar días, minutos, etc.)
yesterday = now - timedelta(days=1)
print("Ayer fue:", yesterday)

tomorrow = now + timedelta(days=1)
print("Mañana será:", tomorrow)

one_hour_later = now + timedelta(hours=1)
print("Dentro de una hora será:", one_hour_later)

# 5. Componentes individuales de una fecha
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(f"Año: {year}, Mes: {month}, Día: {day}, Hora: {hour}, Minuto: {minute}, Segundo: {second}")

# 6. Diferencia entre dos fechas
date1 = datetime.now()
date2 = datetime(2025, 9, 7)
difference = date2 - date1
print("Días de diferencia:", difference.days)
print("Segundos restantes:", difference.seconds)
print("Total segundos restantes:", difference.total_seconds())

