class Persona:
    def __init__(self):
        self.__edad = 0
        self.__nombre = ""
        self.__telefono = ""

  # Gets
    def getEdad(self):
        return self.__edad
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono

  # Sets
    def setEdad(self, edad):
        self.__edad = edad
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setTelefono(self, telefono):
        self.__telefono = telefono

# Crear un objeto persona
persona = Persona()

# Utilizar los sets para asignar valores a las propiedades
persona.setEdad(30)
persona.setNombre("Juan")
persona.setTelefono("555-555-555")

# Mostrar los valores de las propiedades por consola
print(f"La edad de la persona es {persona.getEdad()}")
print(f"El nombre de la persona es {persona.getNombre()}")
print(f"El teléfono de la persona es {persona.getTelefono()}")
