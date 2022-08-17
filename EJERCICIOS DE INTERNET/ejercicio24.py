"""
Escribí un programa que muestre la sumatoria de todos los números entre el 0 y el 100.
"""

i = 0
suma = 0

for i in range (1,101):
    suma = suma + i
    i += 1
print (suma)