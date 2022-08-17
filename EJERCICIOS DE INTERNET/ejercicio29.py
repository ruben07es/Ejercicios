"""
Escribí un programa que permita al usuario ingresar los montos de las compras de un cliente 
(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, 
no se debe procesar y se debe pedir que ingrese un nuevo monto. 
Al finalizar, informar el total a pagar teniendo que cuenta que, 
si las ventas superan el monto total de 1000, se le debe aplicar un 10% de descuento.
"""
total = 0
compra = None
while compra != 0:
    compra = float(input("Compra: "))
    if compra < 0:
        print ("cantidad no procesada")
    else:
        total = total + compra
    
if total > 1000:
    total_final = total - (total * 0.1)
    print (total_final)
else:
    print (total)


