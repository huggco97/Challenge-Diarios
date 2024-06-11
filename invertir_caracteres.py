palabra = input("Ingrese el caracter que desea invertir por favor: ")

def invertir_caracteres(palabra):
    if len(palabra) == 0:
        return ""
    else:
        return palabra[-1] + invertir_caracteres(palabra[:-1])
    
print(invertir_caracteres(palabra))
