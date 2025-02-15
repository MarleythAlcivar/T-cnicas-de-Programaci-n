# Programa para calcular el área de diferentes figuras geométricas sin usar librerías adicionales
# Autor: Marleyth Alcivar
# Descripción: Este programa permite al usuario calcular el área de un círculo, triángulo o rectángulo.

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio sin usar la librería math."""
    pi_aproximado = 3.1416  # Aproximación de pi
    return pi_aproximado * radio * radio

def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dada su base y altura."""
    return 0.5 * base * altura

def calcular_area_rectangulo(largo, ancho):
    """Calcula el área de un rectángulo dado su largo y ancho."""
    return largo * ancho

def menu():
    """Muestra el menú de opciones al usuario."""
    print("\nCalculadora de área")
    print("1. Área de un círculo")
    print("2. Área de un triángulo")
    print("3. Área de un rectángulo")
    print("4. Salir")

# Ciclo principal del programa
while True:
    menu()
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':
        radio = float(input("Ingresa el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
    elif opcion == '2':
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")
    elif opcion == '3':
        largo = float(input("Ingresa el largo del rectángulo: "))
        ancho = float(input("Ingresa el ancho del rectángulo: "))
        area = calcular_area_rectangulo(largo, ancho)
        print(f"El área del rectángulo es: {area:.2f}")
    elif opcion == '4':
        print("Gracias por usar la calculadora de área. Gracias")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 4.")

