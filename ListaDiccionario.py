lista_claves = input("Ingrese palabras separadas por comas: ")
# Divide la cadena de entrada en una lista de palabras usando el método split
lista_claves = lista_claves.split(',')

lista2_valores = input("Ingrese numeros separados por comas: ")
# Divide la cadena de entrada en una lista de números usando el método split y 
# luego convierte cada elemento a un entero
lista2_valores = lista2_valores.split(',')
lista2_valores = [int(valor) for valor in lista2_valores]

# Crea un diccionario combinando las listas de claves y valores usando zip
d = dict(zip(lista_claves, lista2_valores))

print("El diccionario es: ", d)
