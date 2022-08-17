"""
Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa 
y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}


divisa = 0
for i in diccionario:
    divisa = int(input("Seleccione la divisa que quiera mostrar: \n1) Euros, \n2) Dolares \n 3) Yenes: \n"))
    if divisa == 1:
        print (diccionario['Euro'])
    elif divisa == 2:
        print (diccionario ['Dollar'])
    elif divisa == 3:
        print (diccionario['Yen'])
    else:
        print ("Las únicas opciones válidas son 1, 2 o 3")
    