"""
Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número, 
el cual se debe almacenar en una nueva variable. 
Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.
"""

print ("\n #################### EJERCICIO 3 #################### \n")

num1 = input("Introduce el primer número: ")
num2 = input("Introduce el segundo número: ")

suma = int(num1) + int(num2)

print (f"El resultado de la suma es: {suma}")


num3 = input("Introduce el tercer número: ")
multiplicacion = int(suma) * int(num3)

print (f"El resultado de la multiplicación del tercer número con la suma de los 2 primeros es: {multiplicacion}")