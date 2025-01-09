# Sistema de Reservas de Hotel

class Habitacion:
    """Clase que representa una habitación de hotel."""

    def __init__(self, numero, tipo, precio):
        # Inicializa los atributos de la habitación
        self.numero = numero  # Número de habitación
        self.tipo = tipo  # Tipo de habitación (simple, doble, suite)
        self.precio = precio  # Precio por noche
        self.ocupada = False  # Estado de disponibilidad

    def reservar(self):
        """Marca la habitación como ocupada."""
        if not self.ocupada:
            self.ocupada = True
            print(f"La habitación {self.numero} ha sido reservada.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        """Libera la habitación para que esté disponible nuevamente."""
        if self.ocupada:
            self.ocupada = False
            print(f"La habitación {self.numero} ahora está disponible.")
        else:
            print(f"La habitación {self.numero} ya está disponible.")


class Cliente:
    """Clase que representa un cliente."""

    def __init__(self, nombre, documento):
        # Inicializa los atributos del cliente
        self.nombre = nombre  # Nombre del cliente
        self.documento = documento  # Documento de identificación (DNI, pasaporte, etc.)

    def __str__(self):
        """Devuelve una representación en texto del cliente."""
        return f"Cliente: {self.nombre}, Documento: {self.documento}"


class Reserva:
    """Clase que representa una reserva de habitación."""

    def __init__(self, cliente, habitacion, noches):
        # Inicializa los atributos de la reserva
        self.cliente = cliente  # Objeto Cliente
        self.habitacion = habitacion  # Objeto Habitacion
        self.noches = noches  # Número de noches a reservar

    def calcular_costo(self):
        """Calcula el costo total de la reserva."""
        return self.noches * self.habitacion.precio

    def confirmar_reserva(self):
        """Confirma la reserva si la habitación está disponible."""
        if not self.habitacion.ocupada:
            self.habitacion.reservar()
            print(f"Reserva confirmada para {self.cliente.nombre}. Costo total: ${self.calcular_costo():.2f}")
        else:
            print("No se puede confirmar la reserva. La habitación está ocupada.")


# --- Ejemplo de uso ---
# Crear instancias de las clases para simular un sistema de reservas

# Crear algunas habitaciones
habitacion1 = Habitacion(101, "Simple", 50)
habitacion2 = Habitacion(102, "Doble", 80)

# Crear un cliente
cliente1 = Cliente("Ana Perez", "12345678")

# Crear una reserva
reserva1 = Reserva(cliente1, habitacion1, 3)

# Confirmar la reserva
reserva1.confirmar_reserva()

# Intentar reservar nuevamente la misma habitación
reserva2 = Reserva(cliente1, habitacion1, 2)
reserva2.confirmar_reserva()

# Liberar la habitación
habitacion1.liberar()

# Intentar reservar nuevamente después de liberar
reserva2.confirmar_reserva()
