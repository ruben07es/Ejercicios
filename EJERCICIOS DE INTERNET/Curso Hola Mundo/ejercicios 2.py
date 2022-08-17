# multiplicar dos números sin usar el símbolo de multiplicación
"""
num1 = int( input ('Número 1: '))
num2 = int( input ('Número 2: '))

suma = 0

for i in range (num2):
    suma = suma + num1

print (suma)
"""
# ingresar nombre y apellido e imprimirlo al reves
"""
nombre = input ('Nombre: ')
apellido = input ('Apellido: ')

usuario = nombre + ' ' + apellido

print (usuario [::-1])
"""
# escribir una función que encuentre el elemento menor de una lista
from pickle import APPEND

"""
lista = [3,234,65,335,6575,98,0,65889,345]

print ('El número menor es: ', min(lista))

# escribir una función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3
def calcular_volumen (r):
    return 4/3 * 3.14 * r ** 3

resultado = calcular_volumen(6)
print (resultado)
"""
# escribir una función que indique si el usuario es mayor de edad
"""
def mayor_edad (edad):
    
    if edad >= 18:
        return ('Eres mayor de edad')
    else:
        return ('No eres mayor de edad')

edad = int (input ('Introduce tu edad: '))
print (mayor_edad (edad))
# escribir una función que indique si un número es par o impar
def par_impar (num):
    if num%2 == 0:
        return ('El número es par')
    else:
        return ('El número es impar')

num = int (input('Número: '))

print (par_impar (num))
"""

# escribir una función que indique cuantas vocales tiene una palabra
"""
palabra = input('Palabra: ')
vocales = 0
for x in palabra:
    y = x.lower()
    if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u':
        vocales += 1
    

print(vocales)

# escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de los números ingresados
lista = []
basta = ''

while True:
    basta = input('Introduce un número o la palabra "basta" para parar: ')
    if basta == 'basta':
        break
    else:
        basta = int (basta)
        lista.append(basta)

resultado = 0

for x in lista:
    resultado += x

print (resultado)

"""
# escribir una función que reciba nombre y apellido y los vaya agregando a
# un archivo
nombre = input ('Nombre: ')
apellido = input ('Apellido: ')
def texto (nombre, apellido):
    c = open('nombre-completo.doc', 'a')
    c.write (nombre + ' ' + apellido + '\n')
    c.close ()

texto (nombre, apellido)
