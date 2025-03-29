# Ejemplo de Programación Orientada a Objetos en Python

# Clase base (superclase) representando a un Animal
class Animal:
    def __init__(self, nombre, edad):
        # Atributos encapsulados
        self._nombre = nombre  # Usamos _ para indicar que es protegido (no accesible directamente)
        self._edad = edad

    def hacer_sonido(self):
        # Método genérico que será sobrescrito por clases derivadas
        return "Este animal hace un sonido genérico."

    def mostrar_informacion(self):
        # Método para mostrar la información del animal
        return f"Nombre: {self._nombre}, Edad: {self._edad} años"


# Clase derivada (subclase) representando a un Perro, que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamada al constructor de la superclase para inicializar nombre y edad
        super().__init__(nombre, edad)
        self.raza = raza  # Atributo específico de la clase Perro

    def hacer_sonido(self):
        # Sobrescritura del método hacer_sonido (ejemplo de polimorfismo)
        return "Guau! Guau!"

    def mostrar_informacion(self):
        # Polimorfismo: sobrescritura del método para mostrar información más detallada
        return f"Nombre: {self._nombre}, Edad: {self._edad} años, Raza: {self.raza}"


# Clase derivada adicional para otro ejemplo de herencia
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Llamada al constructor de la superclase
        super().__init__(nombre, edad)
        self.color = color  # Atributo específico de la clase Gato

    def hacer_sonido(self):
        # Sobrescritura del método hacer_sonido
        return "Miau!"


# Programa principal para demostrar el uso de las clases
if __name__ == "__main__":
    # Creación de una instancia de la clase Perro
    perro = Perro("Albin", 4, "French Poodle")
    # Creación de una instancia de la clase Gato
    gato = Gato("Dorami", 2, "Café")

    # Uso del método mostrar_informacion de la clase Perro
    print(perro.mostrar_informacion())  # Demostración de herencia y sobrescritura de métodos
    # Uso del método hacer_sonido de la clase Perro
    print(perro.hacer_sonido())  # Demostración de polimorfismo

    # Uso del método mostrar_informacion de la clase Gato
    print(gato.mostrar_informacion())  # Herencia desde la clase base
    # Uso del método hacer_sonido de la clase Gato
    print(gato.hacer_sonido())  # Sobrescritura del método hacer_sonido en la subclase
