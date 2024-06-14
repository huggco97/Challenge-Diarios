
entrada = input("Ingresa una lista de números separados por comas: ")

numeros = list(map(int, entrada.split(',')))

numeros.sort()

print("Lista ordenada:", numeros)
