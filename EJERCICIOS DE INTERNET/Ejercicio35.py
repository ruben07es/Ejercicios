caracter = input("Introduce un caracter: ")
cadena = ""
total = 0
letra = 0
longitud = len(caracter)

if longitud < 2 or caracter == 0:
    if caracter == "a":
        letra += 1
    total += 1
    cadena = cadena + caracter
    caracter = input("Introduce un caracter: ")

a = (letra/total)*100
print (cadena)
print (a)