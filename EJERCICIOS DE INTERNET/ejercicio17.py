"""
Escribí un programa que, dado un número entero, muestre su valor absoluto. 
Recordá que, para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), 
mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
"""

numero = int(input("Introduce el número: "))

if numero < 0:
    print (numero * -1)
else:
    print (numero)