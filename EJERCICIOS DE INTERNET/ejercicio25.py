"""
Escribí un programa que, dada una frase por el usuario, muestre la cantidad total de vocales 
(tanto mayúsculas como minúsculas) que contiene.
"""
frase = input("Introduce la frase: ")

vocales = ["a", "e", "i", "o", "u"]

frase = frase.lower()

for i in frase:
    x = frase.count ("a")
    b = frase.count ("e")
    c = frase.count ("i")
    d = frase.count ("o")
    e = frase.count ("u")

print (x+b+c+d+e)
