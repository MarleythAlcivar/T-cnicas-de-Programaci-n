import uuid


class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.id = f"mm.aa26-{uuid.uuid4()}"  # Genera un ID único con prefijo personalizado
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, cantidad, precio):
        nuevo_producto = Producto(nombre, cantidad, precio)
        self.productos.append(nuevo_producto)

    def eliminar_producto(self, producto_id):
        self.productos = [p for p in self.productos if p.id != producto_id]

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id == producto_id:
                if cantidad is not None:
                    producto.actualizar_cantidad(cantidad)
                if precio is not None:
                    producto.actualizar_precio(precio)
                return

    def buscar_producto(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        return [str(producto) for producto in self.productos]


def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto")
    print("5. Mostrar Inventario")
    print("6. Salir")


def interfaz_usuario():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: $"))
            inventario.agregar_producto(nombre, cantidad, precio)
            print(f"\n{nombre} ha sido agregado al inventario.")

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
            print(f"\nProducto con ID {id_producto} ha sido eliminado.")

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Nuevo precio (deje en blanco para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)
            print(f"\nProducto con ID {id_producto} ha sido actualizado.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto(nombre)
            if productos_encontrados:
                print("\nProductos encontrados:")
                for producto in productos_encontrados:
                    print(producto)
            else:
                print("\nNo se encontraron productos.")

        elif opcion == "5":
            print("\nInventario actual:")
            for producto in inventario.mostrar_productos():
                print(producto)

        elif opcion == "6":
            print("\nGracias por usar el sistema de inventario.")
            break

        else:
            print("\nOpción no válida, por favor intente nuevamente.")


if __name__ == "__main__":
    interfaz_usuario()