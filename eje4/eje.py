class Persona:
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.telefono = ""

class Cliente(Persona):
    def __init__(self):
        self.credito = 0

class Trabajador(Persona):
    def __init__(self):
        self.salario = 0

# Crear un objeto de la clase Cliente
cliente = Cliente()

# Asignar valores a las propiedades del objeto
cliente.edad = 30
cliente.telefono = "555-555-555"
cliente.nombre = "Juan"
cliente.credito = 1000

# Mostrar los valores de las propiedades por consola
print(f"La edad del cliente es {cliente.edad}")
print(f"El teléfono del cliente es {cliente.telefono}")
print(f"El nombre del cliente es {cliente.nombre}")
print(f"El crédito del cliente es {cliente.credito}")

# Crear un objeto de la clase Trabajador
trabajador = Trabajador()

# Asignar valores a las propiedades del objeto
trabajador.edad = 35
trabajador.telefono = "666-666-666"
trabajador.nombre = "Pablo"
trabajador.salario = 2000

# Mostrar los valores de las propiedades por consola
print(f"La edad del trabajador es {trabajador.edad}")
print(f"El teléfono del trabajador es {trabajador.telefono}")
print(f"El nombre del trabajador es {trabajador.nombre}")
print(f"El salario del trabajador es {trabajador.salario}")
