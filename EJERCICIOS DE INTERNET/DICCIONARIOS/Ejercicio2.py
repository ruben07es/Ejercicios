"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>.
"""


info = {'Nombre':'','Edad': 0,'Direccion': '', 'Telefono': 0}

nombre = input ("Dime tu nombre: ")
edad = int(input("Dime tu edad: "))
direccion = input ("Pon tu dirección: ")
telefono = int (input("Pon tu nº de telefono: "))


info['Nombre'] = nombre
info['Edad'] = edad
info ['Dirección'] = direccion
info['Teléfono'] = telefono

print (info)