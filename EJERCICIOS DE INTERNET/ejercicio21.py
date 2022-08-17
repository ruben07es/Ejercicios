"""
Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. 
Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
"""

nombre_usuario = input("Introduce tu nombre de usuario: ")
password_usuario = input("Introduce tu contraseña: ")

usuario = "Gwenevere"
password = "excalibur"

if nombre_usuario == usuario and password_usuario == password:
    print ("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print ("Acceso denegado")