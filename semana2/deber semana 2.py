# Clase base
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre  # Atributo público
        self.__energia = 100  # Atributo privado

    def comer(self):
        """Incrementa la energía del animal."""
        self.__energia += 10
        print(f"{self.nombre} ha comido y ahora tiene {self.__energia} de energía.")

    def hacer_sonido(self):
        """Método para sobrescribir en clases hijas."""
        pass

    def estado(self):
        """Muestra el estado del animal."""
        print(f"{self.nombre} tiene {self.__energia} de energía.")

# Clase derivada: Perro
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre, "Ladrido")
        self.raza = raza

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def jugar(self):
        print(f"{self.nombre} está jugando. Pierde energía...")
        self._Animal__energia -= 15  # Accediendo al atributo privado de la clase base

# Clase derivada: Gato
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre, "Maullido")
        self.color = color

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def dormir(self):
        print(f"{self.nombre} está durmiendo y recupera energía.")
        self._Animal__energia += 20

# Uso del polimorfismo
def interactuar_con_animal(animal):
    animal.hacer_sonido()
    animal.estado()

# Creación de objetos
perro = Perro("Max", "Labrador")
gato = Gato("Luna", "Blanco")

# Interacción con los objetos
print("---- Interacción con el perro ----")
perro.hacer_sonido()
perro.jugar()
perro.estado()

print("\n---- Interacción con el gato ----")
gato.hacer_sonido()
gato.dormir()
gato.estado()

print("\n---- Polimorfismo ----")
animales = [perro, gato]
for animal in animales:
    interactuar_con_animal(animal)
