class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Los atributos autor y título son inmutables, por lo que utilizamos tuplas
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, ISBN: {self.isbn}, Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        # Cada usuario tiene un nombre, ID único y una lista de libros prestados
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        # Usamos un diccionario para almacenar libros por ISBN y un conjunto para IDs de usuarios únicos
        self.libros = {}
        self.usuarios = set()

    def añadir_libro(self, libro):
        """Añadir un libro a la biblioteca."""
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        """Quitar un libro de la biblioteca."""
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado de la biblioteca.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registrar un nuevo usuario en la biblioteca."""
        if usuario.id_usuario not in [u.id_usuario for u in self.usuarios]:
            self.usuarios.add(usuario)
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        """Dar de baja a un usuario de la biblioteca."""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario '{usuario.nombre}' dado de baja.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        """Prestar un libro a un usuario."""
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if libro and usuario and isbn not in [l.isbn for l in usuario.libros_prestados]:
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("El libro no está disponible o el usuario no está registrado.")

    def devolver_libro(self, id_usuario, isbn):
        """Devolver un libro prestado."""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
            else:
                print("El libro no fue prestado a este usuario.")
        else:
            print("El usuario no está registrado.")

    def buscar_libro(self, busqueda):
        """Buscar libros por título, autor o categoría."""
        resultados = [libro for libro in self.libros.values()
                      if busqueda.lower() in libro.titulo.lower() or
                      busqueda.lower() in libro.autor.lower() or
                      busqueda.lower() in libro.categoria.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")

    def listar_libros_prestados(self, id_usuario):
        """Listar todos los libros prestados a un usuario."""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("El usuario no está registrado.")


# Pruebas del sistema

# Crear libros
libro1 = Libro("Una Mujer Conforme Al Corazon de Dios", "Elizabeth George", "Religión", "9780307474728")
libro2 = Libro("Un Líder No Nace, Se Hace", "Ted W. Engstrom", "Liderazgo", "9788491051195")
libro3 = Libro("Esperanza Para El Corazón Afligido", "Billy Graham", "Inspiracional", "9780140268867")

# Crear usuarios
usuario1 = Usuario("Marleyth Alcivar", "001")
usuario2 = Usuario("Tommy Alava", "002")

# Crear biblioteca
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("001", "9780307474728")  # Marleyth Alcivar pide Una Mujer Conforme Al Corazon de Dios
biblioteca.prestar_libro("002", "9788491051195")  # Tommy Alava pide Un Líder No Nace, Se Hace

# Devolver libro
biblioteca.devolver_libro("001", "9780307474728")  # Marleyth Alcivar devuelve Una Mujer Conforme Al Corazon de Dios

# Buscar libros
biblioteca.buscar_libro("Mujer")  # Buscar por título

# Listar libros prestados
biblioteca.listar_libros_prestados("002")  # Listar libros prestados a Tommy Alava
