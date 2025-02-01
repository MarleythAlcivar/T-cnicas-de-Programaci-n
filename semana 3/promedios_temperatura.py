# --- Programación Tradicional ---
# Este enfoque utiliza funciones para organizar el flujo del programa.

def ingresar_temperaturas(datos):
    """
    Función para procesar temperaturas diarias durante 7 días.
    Retorna una lista con las temperaturas ingresadas.
    """
    print("Procesando las temperaturas diarias (una para cada día de la semana):")
    temperaturas = []
    for i, temp in enumerate(datos):
        print(f"Día {i + 1}: {temp}°C")
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Función que calcula el promedio de una lista de temperaturas.
    """
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Flujo principal del programa
print("--- Cálculo del promedio semanal de temperaturas (Programación Tradicional) ---")
datos_ejemplo = [25.0, 26.5, 24.0, 23.5, 27.0, 28.0, 26.0]  # Ejemplo de datos predefinidos
temperaturas_semanales = ingresar_temperaturas(datos_ejemplo)
promedio_semanal = calcular_promedio(temperaturas_semanales)
print(f"El promedio semanal de temperaturas es: {promedio_semanal:.2f}°C")

# --- Programación Orientada a Objetos (POO) ---
# Este enfoque utiliza clases y métodos para organizar el programa.

class Clima:
    """
    Clase que representa las temperaturas diarias y realiza cálculos relacionados.
    """
    def __init__(self):
        # Atributo privado que almacena las temperaturas de la semana
        self.__temperaturas = []

    def ingresar_temperaturas(self, datos):
        """
        Método para procesar temperaturas diarias durante 7 días.
        """
        print("Procesando las temperaturas diarias (una para cada día de la semana):")
        for i, temp in enumerate(datos):
            print(f"Día {i + 1}: {temp}°C")
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula el promedio de las temperaturas almacenadas.
        """
        if not self.__temperaturas:
            return 0.0  # Retorna 0 si no hay temperaturas ingresadas
        promedio = sum(self.__temperaturas) / len(self.__temperaturas)
        return promedio

# Flujo principal del programa orientado a objetos
print("\n--- Cálculo del promedio semanal de temperaturas (POO) ---")
datos_ejemplo_poo = [25.0, 26.5, 24.0, 23.5, 27.0, 28.0, 26.0]  # Ejemplo de datos predefinidos
clima_semanal = Clima()  # Creamos una instancia de la clase Clima
clima_semanal.ingresar_temperaturas(datos_ejemplo_poo)  # Llamamos al método para procesar datos
temperatura_promedio = clima_semanal.calcular_promedio()  # Calculamos el promedio
print(f"El promedio semanal de temperaturas es: {temperatura_promedio:.2f}°C")
