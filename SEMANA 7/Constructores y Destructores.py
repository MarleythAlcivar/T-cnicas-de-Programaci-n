# Programa en Python demostrando el uso de constructores (__init__) y destructores (__del__)
class GestorDeArchivos:
    """
    Clase para gestionar la lectura y escritura de archivos.
    Utiliza un constructor para inicializar atributos y abrir un archivo,
    y un destructor para cerrar el archivo automáticamente.
    """

    def __init__(self, nombre_archivo, modo):
        """
        Constructor que inicializa los atributos de la clase y abre el archivo.
        :param nombre_archivo: Nombre del archivo a gestionar.
        :param modo: Modo en el que se abrirá el archivo (lectura, escritura, etc.).
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        try:
            self.archivo = open(self.nombre_archivo, self.modo)
            print(f"Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            self.archivo = None

    def escribir_datos(self, datos):
        """
        Método para escribir datos en el archivo.
        :param datos: Cadena de texto a escribir en el archivo.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.write(datos + '\n')
            print(f"Datos escritos en el archivo '{self.nombre_archivo}'.")
        else:
            print("No se puede escribir en el archivo porque no está abierto.")

    def leer_datos(self):
        """
        Método para leer datos del archivo.
        :return: Contenido del archivo como una lista de líneas.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.seek(0)  # Reinicia el puntero al inicio del archivo.
            return self.archivo.readlines()
        else:
            print("No se puede leer del archivo porque no está abierto.")
            return []

    def __del__(self):
        """
        Destructor que cierra el archivo cuando el objeto es eliminado.
        """
        if self.archivo and not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")

# Demostración del uso de constructores y destructores
if __name__ == "__main__":
    # Crear una instancia de GestorDeArchivos y escribir datos
    gestor = GestorDeArchivos("ejemplo.txt", "w+")
    gestor.escribir_datos("Línea 1: Este es un ejemplo.")
    gestor.escribir_datos("Línea 2: Demostración de constructores y destructores.")

    # Leer los datos del archivo
    print("Contenido del archivo:")
    for linea in gestor.leer_datos():
        print(linea.strip())

    # El archivo se cerrará automáticamente cuando el objeto sea eliminado.
