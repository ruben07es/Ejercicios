numero = int (input ("Número: "))

mayor = -1
while numero != 0:
    if numero > mayor:
        mayor = numero
    numero = int (input ("Número: "))

print (mayor)