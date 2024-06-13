def contar_vocales(palabra1):
    vocales = "aeiou"
    contador = 0
    for caracter in palabra:
        if caracter in vocales:
            contador += 1
    
    return contador


palabra = input("Ingrese una palbra por favor ")
palabra1 = palabra.lower
num_vocales = contar_vocales(palabra1)
print(f"El número de vocales en la palabra es: {num_vocales}")
