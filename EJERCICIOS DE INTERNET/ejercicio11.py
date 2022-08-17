"""
Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, 
donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). 
Este dato debe guardarse en una variable con tipo int (número entero). 
Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.
"""

print ("\n #################### EJERCICIO 11 #################### \n")

fecha = int(input("Introduce una fecha con formato DDMMAAAA: "))

dia = int(fecha/1000000)
mes = int(fecha/10000) - (dia*100)
#año = int(fecha -)

print (dia)
print (mes)
print (año)
#print (f"La fecha es: {dia}/{mes}/{año}")