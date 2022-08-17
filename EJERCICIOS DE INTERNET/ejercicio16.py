"""
Escribí un programa para pedir al usuario su nombre y luego el nombre de otra persona, 
almacenando cada nombre en una variable. Luego mostrar en pantalla un valor de verdad que indique si: 
los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. 
Por ejemplo, si los nombres ingresados son María y Marcos, se mostrará True, ya que ambos comienzan con la misma letra. 
Si los nombres son Ricardo y Gonzalo se mostrará True, ya que ambos terminan con la misma letra. 
Si los nombres son Florencia y Lautaro se mostrará False, ya que no coinciden ni la primera ni la última letra.
"""



print ("\n #################### EJERCICIO 16 #################### \n")

Nombre = input("Introduce el primer nombre: ")
Nombre2 = input("Introduce el segundo nombre: ")
longitud1 = len(Nombre)-1
longitud2 = len(Nombre2)-1

if Nombre[0]==Nombre2[0] or Nombre[longitud1]==Nombre2[longitud2]:
    print (True)
else:
    print (False)
