"""
Dado un listado de números, encuentra el SEGUNDO más grande.
"""

lista = []
a = ''
while a != 'comprobar':
    a = input ('Introduce el número a añadir: ')
    if a == 'comprobar':
        break
    lista.append(a)
lista.sort()
print (lista[-1])