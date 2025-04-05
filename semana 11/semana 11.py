import os
import json
from typing import Dict, List, Optional, Union


class Producto:
    """
    Clase que representa un producto en el inventario.
    """

    def __init__(self, id: str, nombre: str, cantidad: int, precio: float):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    @property
    def id(self) -> str:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value: int) -> None:
        if value < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = value

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, value: float) -> None:
        if value < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = value

    def __str__(self) -> str:
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"

    def to_dict(self) -> Dict:
        """Convierte el producto a un diccionario para serialización."""
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Producto':
        """Crea un objeto Producto desde un diccionario."""
        return cls(
            id=data["id"],
            nombre=data["nombre"],
            cantidad=data["cantidad"],
            precio=data["precio"]
        )


class Inventario:
    """
    Clase que gestiona la colección de productos.
    """

    def __init__(self):
        self._productos: Dict[str, Producto] = {}

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Agrega un nuevo producto al inventario.
        Retorna True si se agregó correctamente, False si ya existe un producto con ese ID.
        """
        if producto.id in self._productos:
            return False

        self._productos[producto.id] = producto
        return True

    def eliminar_producto(self, id_producto: str) -> bool:
        """
        Elimina un producto del inventario por su ID.
        Retorna True si se eliminó correctamente, False si no existe.
        """
        if id_producto in self._productos:
            del self._productos[id_producto]
            return True
        return False

    def actualizar_cantidad(self, id_producto: str, nueva_cantidad: int) -> bool:
        """
        Actualiza la cantidad de un producto.
        Retorna True si se actualizó correctamente, False si no existe.
        """
        if id_producto in self._productos:
            self._productos[id_producto].cantidad = nueva_cantidad
            return True
        return False

    def actualizar_precio(self, id_producto: str, nuevo_precio: float) -> bool:
        """
        Actualiza el precio de un producto.
        Retorna True si se actualizó correctamente, False si no existe.
        """
        if id_producto in self._productos:
            self._productos[id_producto].precio = nuevo_precio
            return True
        return False

    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        """
        Busca productos que contengan el nombre especificado.
        Retorna una lista de productos que coinciden con la búsqueda.
        """
        nombre = nombre.lower()
        return [p for p in self._productos.values() if nombre in p.nombre.lower()]

    def obtener_producto(self, id_producto: str) -> Optional[Producto]:
        """
        Obtiene un producto por su ID.
        """
        return self._productos.get(id_producto)

    def listar_productos(self) -> List[Producto]:
        """
        Retorna una lista con todos los productos en el inventario.
        """
        return list(self._productos.values())

    def guardar_en_archivo(self, ruta_archivo: str) -> bool:
        """
        Guarda el inventario en un archivo JSON.
        """
        try:
            # Convertir productos a diccionarios
            productos_dict = {id: producto.to_dict() for id, producto in self._productos.items()}

            # Crear directorio si no existe
            os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

            with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(productos_dict, archivo, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")
            return False

    def cargar_desde_archivo(self, ruta_archivo: str) -> bool:
        """
        Carga el inventario desde un archivo JSON.
        """
        try:
            if not os.path.exists(ruta_archivo):
                return False

            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                productos_dict = json.load(archivo)

            # Limpiar inventario actual
            self._productos.clear()

            # Cargar productos desde el diccionario
            for id, datos in productos_dict.items():
                self._productos[id] = Producto.from_dict(datos)
            return True
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
            return False


class SistemaInventario:
    """
    Clase que maneja la interfaz de usuario y la lógica del sistema.
    """

    def __init__(self, ruta_archivo: str = "datos/inventario.json"):
        self.inventario = Inventario()
        self.ruta_archivo = ruta_archivo
        # Intentar cargar datos existentes
        self.inventario.cargar_desde_archivo(self.ruta_archivo)

    def menu_principal(self) -> None:
        """
        Muestra el menú principal y maneja la interacción con el usuario.
        """
        opciones = {
            "1": "Agregar producto",
            "2": "Eliminar producto",
            "3": "Actualizar cantidad",
            "4": "Actualizar precio",
            "5": "Buscar productos por nombre",
            "6": "Ver todos los productos",
            "7": "Guardar inventario",
            "8": "Cargar inventario",
            "9": "Salir"
        }

        while True:
            print("\n===== SISTEMA DE GESTIÓN DE INVENTARIO =====")
            for key, value in opciones.items():
                print(f"{key}. {value}")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self.agregar_producto()
            elif opcion == "2":
                self.eliminar_producto()
            elif opcion == "3":
                self.actualizar_cantidad()
            elif opcion == "4":
                self.actualizar_precio()
            elif opcion == "5":
                self.buscar_por_nombre()
            elif opcion == "6":
                self.ver_todos_productos()
            elif opcion == "7":
                self.guardar_inventario()
            elif opcion == "8":
                self.cargar_inventario()
            elif opcion == "9":
                # Guardar automáticamente antes de salir
                self.inventario.guardar_en_archivo(self.ruta_archivo)
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def agregar_producto(self) -> None:
        """
        Solicita información para agregar un nuevo producto.
        """
        print("\n--- Agregar Nuevo Producto ---")

        # Solicitar datos del producto
        id_producto = input("ID del producto: ").strip()

        # Verificar si el ID ya existe
        if self.inventario.obtener_producto(id_producto):
            print(f"Error: Ya existe un producto con el ID {id_producto}")
            return

        nombre = input("Nombre del producto: ").strip()

        # Validar cantidad
        try:
            cantidad = int(input("Cantidad (unidades): "))
            if cantidad < 0:
                print("Error: La cantidad no puede ser negativa")
                return
        except ValueError:
            print("Error: La cantidad debe ser un número entero")
            return

        # Validar precio
        try:
            precio = float(input("Precio unitario: $"))
            if precio < 0:
                print("Error: El precio no puede ser negativo")
                return
        except ValueError:
            print("Error: El precio debe ser un número")
            return

        # Crear y agregar el producto
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        if self.inventario.agregar_producto(nuevo_producto):
            print(f"Producto '{nombre}' agregado correctamente")
        else:
            print("Error al agregar el producto")

    def eliminar_producto(self) -> None:
        """
        Solicita el ID del producto a eliminar.
        """
        print("\n--- Eliminar Producto ---")
        id_producto = input("ID del producto a eliminar: ").strip()

        if self.inventario.eliminar_producto(id_producto):
            print("Producto eliminado correctamente")
        else:
            print(f"Error: No se encontró ningún producto con el ID {id_producto}")

    def actualizar_cantidad(self) -> None:
        """
        Actualiza la cantidad de un producto existente.
        """
        print("\n--- Actualizar Cantidad ---")
        id_producto = input("ID del producto: ").strip()

        producto = self.inventario.obtener_producto(id_producto)
        if not producto:
            print(f"Error: No se encontró ningún producto con el ID {id_producto}")
            return

        print(f"Producto actual: {producto}")

        # Validar nueva cantidad
        try:
            nueva_cantidad = int(input("Nueva cantidad: "))
            if nueva_cantidad < 0:
                print("Error: La cantidad no puede ser negativa")
                return
        except ValueError:
            print("Error: La cantidad debe ser un número entero")
            return

        if self.inventario.actualizar_cantidad(id_producto, nueva_cantidad):
            print("Cantidad actualizada correctamente")
        else:
            print("Error al actualizar la cantidad")

    def actualizar_precio(self) -> None:
        """
        Actualiza el precio de un producto existente.
        """
        print("\n--- Actualizar Precio ---")
        id_producto = input("ID del producto: ").strip()

        producto = self.inventario.obtener_producto(id_producto)
        if not producto:
            print(f"Error: No se encontró ningún producto con el ID {id_producto}")
            return

        print(f"Producto actual: {producto}")

        # Validar nuevo precio
        try:
            nuevo_precio = float(input("Nuevo precio: $"))
            if nuevo_precio < 0:
                print("Error: El precio no puede ser negativo")
                return
        except ValueError:
            print("Error: El precio debe ser un número")
            return

        if self.inventario.actualizar_precio(id_producto, nuevo_precio):
            print("Precio actualizado correctamente")
        else:
            print("Error al actualizar el precio")

    def buscar_por_nombre(self) -> None:
        """
        Busca productos por nombre y muestra los resultados.
        """
        print("\n--- Buscar Productos por Nombre ---")
        nombre_busqueda = input("Término de búsqueda: ").strip()

        resultados = self.inventario.buscar_por_nombre(nombre_busqueda)

        if resultados:
            print(f"\nSe encontraron {len(resultados)} productos:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre")

    def ver_todos_productos(self) -> None:
        """
        Muestra todos los productos en el inventario.
        """
        print("\n--- Lista de Productos en Inventario ---")
        productos = self.inventario.listar_productos()

        if productos:
            for i, producto in enumerate(productos, 1):
                print(f"{i}. {producto}")
            print(f"\nTotal de productos: {len(productos)}")
        else:
            print("El inventario está vacío")

    def guardar_inventario(self) -> None:
        """
        Guarda el inventario en el archivo.
        """
        print("\n--- Guardar Inventario ---")
        if self.inventario.guardar_en_archivo(self.ruta_archivo):
            print(f"Inventario guardado correctamente en '{self.ruta_archivo}'")
        else:
            print("Error al guardar el inventario")

    def cargar_inventario(self) -> None:
        """
        Carga el inventario desde el archivo.
        """
        print("\n--- Cargar Inventario ---")
        if self.inventario.cargar_desde_archivo(self.ruta_archivo):
            print(f"Inventario cargado correctamente desde '{self.ruta_archivo}'")
        else:
            print(f"No se pudo cargar el inventario desde '{self.ruta_archivo}'")


def main():
    """
    Función principal que inicia el sistema.
    """
    sistema = SistemaInventario()
    sistema.menu_principal()


if __name__ == "__main__":
    main()
