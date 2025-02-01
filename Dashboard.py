import os


def listar_archivos_python(base_path):
    opciones = {}
    indice = 1
    for carpeta in sorted(os.listdir(base_path)):
        carpeta_path = os.path.join(base_path, carpeta)
        if os.path.isdir(carpeta_path):
            for archivo in sorted(os.listdir(carpeta_path)):
                if archivo.endswith(".py"):
                    ruta_script = os.path.join(carpeta_path, archivo)
                    opciones[str(indice)] = ruta_script
                    indice += 1
    return opciones


def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    opciones = listar_archivos_python(ruta_base)

    while True:
        print("\n******** Menu Principal - Dashboard *************")
        for key, path in opciones.items():
            print(f"{key} - {path}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            mostrar_codigo(opciones[eleccion])
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    mostrar_menu()
