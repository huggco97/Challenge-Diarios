
import string
import secrets

# Función para obtener una longitud válida
def obtener_longitud():
    while True:
        try:
            longitud = int(input("Ingrese la longitud para la contraseña, debe ser de 8 a 16: "))
            if 8 <= longitud <= 16:
                return longitud
            else:
                print("Por favor, ingrese un valor entre 8 y 16.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Obtenemos una longitud válida
longitud = obtener_longitud()

# Definimos conjuntos de caracteres a utilizar
caracteres = string.ascii_letters + string.digits + string.punctuation

# Creamos una lista vacía para almacenar los caracteres de la contraseña
password = []

# Añadimos al menos un carácter de cada tipo (minúscula, mayúscula, número y especial) a la contraseña
password.append(secrets.choice(string.ascii_lowercase))  # Añadimos una minúscula
password.append(secrets.choice(string.ascii_uppercase))  # Añadimos una mayúscula
password.append(secrets.choice(string.digits))           # Añadimos un número
password.append(secrets.choice(string.punctuation))      # Añadimos un carácter especial

# Completamos la contraseña con caracteres aleatorios hasta alcanzar la longitud deseada
while len(password) < longitud:
    password.append(secrets.choice(caracteres))  # Usamos secrets.choice para mayor seguridad

# Mezclamos los caracteres de la contraseña para evitar patrones predecibles
secrets.SystemRandom().shuffle(password)

# Convertimos la lista de caracteres en una cadena
password = "".join(password)

# Mostramos la contraseña generada
print("Contraseña generada:", password)



