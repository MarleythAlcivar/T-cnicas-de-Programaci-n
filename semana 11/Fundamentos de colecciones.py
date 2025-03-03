# sistema_inventario.py
# Este programa permite gestionar un inventario de productos
# usando archivos CSV para almacenar los datos

import csv
import os


# Clase para representar un producto
class Producto:
    # Constructor de la clase
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Método para mostrar el producto como texto
    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


# Clase para gestionar el inventario
class Inventario:
    # Constructor de la clase
    def __init__(self):
        # Lista para almacenar los productos
        self.productos = []

    # Método para agregar un producto
    def agregar_producto(self, producto):
        # Verificar si el ID ya existe
        for p in self.productos:
            if p.id == producto.id:
                print("Error: Ya existe un producto con ese ID")
                return False

        # Agregar el producto a la lista
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado con éxito")
        return True

    # Método para eliminar un producto
    def eliminar_producto(self, id):
        # Buscar el producto por ID
        for i, producto in enumerate(self.productos):
            if producto.id == id:
                # Eliminar el producto de la lista
                self.productos.pop(i)
                print(f"Producto con ID {id} eliminado con éxito")
                return True

        print(f"No se encontró ningún producto con ID {id}")
        return False

    # Método para actualizar la cantidad de un producto
    def actualizar_cantidad(self, id, nueva_cantidad):
        # Buscar el producto por ID
        for producto in self.productos:
            if producto.id == id:
                # Actualizar la cantidad
                producto.cantidad = nueva_cantidad
                print(f"Cantidad actualizada para el producto {producto.nombre}")
                return True

        print(f"No se encontró ningún producto con ID {id}")
        return False

    # Método para actualizar el precio de un producto
    def actualizar_precio(self, id, nuevo_precio):
        # Buscar el producto por ID
        for producto in self.productos:
            if producto.id == id:
                # Actualizar el precio
                producto.precio = nuevo_precio
                print(f"Precio actualizado para el producto {producto.nombre}")
                return True

        print(f"No se encontró ningún producto con ID {id}")
        return False

    # Método para buscar productos por nombre
    def buscar_por_nombre(self, nombre):
        # Lista para almacenar los resultados
        resultados = []

        # Buscar productos que contengan el nombre
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():
                resultados.append(producto)

        return resultados

    # Método para obtener todos los productos
    def listar_productos(self):
        return self.productos

    # Método para guardar el inventario en un archivo CSV
    def guardar_en_archivo(self, nombre_archivo="inventario.csv"):
        try:
            # Abrir el archivo en modo escritura
            with open(nombre_archivo, 'w', newline='') as archivo:
                # Crear el escritor CSV
                escritor = csv.writer(archivo)

                # Escribir la cabecera
                escritor.writerow(['id', 'nombre', 'cantidad', 'precio'])

                # Escribir los datos de cada producto
                for producto in self.productos:
                    escritor.writerow([producto.id, producto.nombre, producto.cantidad, producto.precio])

            print(f"Inventario guardado en {nombre_archivo}")
            return True
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
            return False

    # Método para cargar el inventario desde un archivo CSV
    def cargar_desde_archivo(self, nombre_archivo="inventario.csv"):
        # Verificar si el archivo existe
        if not os.path.exists(nombre_archivo):
            print(f"El archivo {nombre_archivo} no existe. Se creará al guardar.")
            return False

        try:
            # Limpiar la lista actual
            self.productos = []

            # Abrir el archivo en modo lectura
            with open(nombre_archivo, 'r', newline='') as archivo:
                # Crear el lector CSV
                lector = csv.reader(archivo)

                # Saltar la cabecera
                next(lector)

                # Leer cada línea y crear los productos
                for fila in lector:
                    if len(fila) >= 4:
                        id = fila[0]
                        nombre = fila[1]
                        # Convertir cantidad a entero
                        try:
                            cantidad = int(fila[2])
                        except ValueError:
                            cantidad = 0

                        # Convertir precio a float
                        try:
                            precio = float(fila[3])
                        except ValueError:
                            precio = 0.0

                        # Crear el producto y agregarlo a la lista
                        producto = Producto(id, nombre, cantidad, precio)
                        self.productos.append(producto)

            print(f"Inventario cargado desde {nombre_archivo}")
            return True
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            return False


# Función principal del programa
def main():
    # Crear el inventario
    inventario = Inventario()

    # Cargar datos desde el archivo (si existe)
    inventario.cargar_desde_archivo()

    # Variable para controlar el ciclo principal
    ejecutando = True

    # Ciclo principal del programa
    while ejecutando:
        # Mostrar el menú
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar por nombre")
        print("6. Mostrar todos los productos")
        print("7. Guardar y salir")
        print("================================")

        # Obtener la opción del usuario
        opcion = input("Seleccione una opción (1-7): ")

        # Procesar la opción
        if opcion == "1":
            # Agregar producto
            print("\n-- AGREGAR PRODUCTO --")
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")

            # Validar cantidad
            while True:
                cantidad_str = input("Cantidad: ")
                try:
                    cantidad = int(cantidad_str)
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa")
                    else:
                        break
                except ValueError:
                    print("Por favor ingrese un número válido")

            # Validar precio
            while True:
                precio_str = input("Precio: $")
                try:
                    precio = float(precio_str)
                    if precio <= 0:
                        print("El precio debe ser mayor que cero")
                    else:
                        break
                except ValueError:
                    print("Por favor ingrese un número válido")

            # Crear y agregar el producto
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            # Eliminar producto
            print("\n-- ELIMINAR PRODUCTO --")
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            # Actualizar cantidad
            print("\n-- ACTUALIZAR CANTIDAD --")
            id = input("ID del producto: ")

            # Validar cantidad
            while True:
                cantidad_str = input("Nueva cantidad: ")
                try:
                    cantidad = int(cantidad_str)
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa")
                    else:
                        break
                except ValueError:
                    print("Por favor ingrese un número válido")

            inventario.actualizar_cantidad(id, cantidad)

        elif opcion == "4":
            # Actualizar precio
            print("\n-- ACTUALIZAR PRECIO --")
            id = input("ID del producto: ")

            # Validar precio
            while True:
                precio_str = input("Nuevo precio: $")
                try:
                    precio = float(precio_str)
                    if precio <= 0:
                        print("El precio debe ser mayor que cero")
                    else:
                        break
                except ValueError:
                    print("Por favor ingrese un número válido")

            inventario.actualizar_precio(id, precio)

        elif opcion == "5":
            # Buscar por nombre
            print("\n-- BUSCAR POR NOMBRE --")
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print(f"\nSe encontraron {len(resultados)} productos:")
                for i, producto in enumerate(resultados, 1):
                    print(f"{i}. {producto}")
            else:
                print("No se encontraron productos con ese nombre")

        elif opcion == "6":
            # Mostrar todos los productos
            print("\n-- LISTA DE PRODUCTOS --")
            productos = inventario.listar_productos()

            if productos:
                print(f"Total: {len(productos)} productos")
                for i, producto in enumerate(productos, 1):
                    print(f"{i}. {producto}")
            else:
                print("El inventario está vacío")

        elif opcion == "7":
            # Guardar y salir
            inventario.guardar_en_archivo()
            print("¡Gracias por usar el sistema!")
            ejecutando = False

        else:
            print("Opción no válida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()