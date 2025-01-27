# La vercion de python que vamos a estuidar es la 3.10, esta vercion de python hay una característica introducida  como pattern matching.
# Es similar a los switch-case de otros lenguajes, pero mucho más poderoso. Sirve para comparar estructuras de datos complejas, como diccionarios o listas,
# con patrones específicos.

# Ejemplo de match
def process_command(command):
    match command:
        case "start":
            return "Starting the system..."
        case "stop":
            return "Stopping the system..."
        case "restart":
            return "Restarting the system..."
        case _:
            return "Unknown command!"


print(process_command("start"))  # Output: Starting the system...
print(process_command("unknown"))  # Output: Unknown command!

# Ejemplo de match con patrones


def process_command2(command):
    match command:
        case "start" | "restart":
            return "Starting the system..."
        case "stop":
            return "Stopping the system..."
        case _:
            return "Unknown command!"


print(process_command2("restart"))  # Output: Starting the system...
print(process_command2("stop"))  # Output: Stopping the system...

# La diferencia con if y match es que match es más limpio y fácil de leer, y es más fácil de agregar más casos.
# También es más fácil de mantener, ya que si queremos agregar más casos, solo necesitamos agregar más líneas de código,
# en lugar de agregar más condiciones.

# Ejemplo de match con patrones y variables


def matcheo(data):
    match data:
        case (username, "admin"):
            print(f"Welcome back, admin {username}!")
        case (username, role):
            print(f"Hello, {username}. Your role is {role}.")


data = ("user123", "admin")
matcheo(data)
data = ("user123", "user")
matcheo(data)

# Tips: Puedes usar como comodin _ para ignorar valores que no te interesan.
# Tips: Puedes usar | para hacer un OR entre dos valores.
# Tips: Puedes usar : para asignar un valor a una variable.

# Ejemplo de : para asignar un valor a una variable
items = [1, 2, 3, 4]

match items:
    case [first, second, *rest]:
        print(f"First: {first}, Second: {second}, Rest: {rest}")
    case _:
        print("Pattern did not match.")

# Ejempo con diccionarios
cliente = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30,
    "email": "juanperez@gmail.com"
}

pelicula = {
    "titulo": "Titanic",
    "director": "James Cameron",
    "año": 1997
}

elementos = [cliente, pelicula, "CD"]

for elemento in elementos:
    match elemento:
        case {"nombre": name, "apellido": last_name}:
            print(f"Cliente: {name} {last_name}")
        case {"titulo": title, "director": director}:
            print(f"Pelicula: {title} de {director}")
        case _:
            print(f"Elemento: {elemento}")
