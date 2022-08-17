"""
Escribí un programa que muestre los primeros 10 números de la sucesión de Fibonacci. 
La sucesión comienza con los números 0 y 1 y, a partir de éstos, 
cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
"""
from termios import NL1


n = 0
n1 = 1
print (n)
print (n1)

for i in range (8):
    n2 = n + n1
    print (n2)
    n = n1
    n1 = n2