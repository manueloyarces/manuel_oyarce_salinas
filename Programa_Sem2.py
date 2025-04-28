# FUNCION para calcular el descuento en la compra de licencias
def calcular_descuento(cantidad_licencias):
    precio_base = 50  # Precio base por cada licencia
    if cantidad_licencias >= 5:
        descuento = 0.30
    elif cantidad_licencias >= 3:
        descuento = 0.20
    else:
        descuento = 0.0
    # Cálculo del precio total con descuento incluido
    precio_total = cantidad_licencias * precio_base * (1 - descuento)
    return precio_total

# FUNCION para calcular el volumen de una esfera
def calcular_volumen_esfera(radio):
    pi = 3.1416  # Constante de pi
    volumen = (4 / 3) * pi * (radio ** 3)  # Fórmula del volumen
    return volumen

# FUNCION para mostrar el menú principal
def menu():
    print("\nBienvenido al programa de MyPro")
    print("1. Calcular descuento en compras de software")
    print("2. Calcular el volumen de una esfera")
    print("3. Salir del Programa")
    opcion = input("Seleccione una opción (1, 2, o 3): ")
    return opcion

# FUNCION principal que ejecuta el programa
def main():
    while True:
        opcion = menu()
        if opcion == "1":
            # Opción para calcular descuento
            try:
                cantidad = int(input("Ingrese la cantidad de licencias a comprar: "))
                if cantidad < 0:
                    print("La cantidad debe ser un número positivo.")
                else:
                    total = calcular_descuento(cantidad)
                    print(f"El precio total con descuento incluido es: ${total:.2f}")
            except ValueError:
                print("Ingrese un número válido.")
        
        elif opcion == "2":
            # Opción para calcular volumen de una esfera
            try:
                radio = float(input("Ingrese el radio de la esfera: "))
                if radio < 0:
                    print("El radio debe ser un número positivo.")
                else:
                    volumen = calcular_volumen_esfera(radio)
                    print(f"El volumen de la esfera es: {volumen:.2f} unidades cúbicas.")
            except ValueError:
                print("Ingrese un número válido.")
        
        elif opcion == "3":
            # Salir del programa
            print("Gracias por utilizar el programa. ¡Hasta Pronto!")
            break
        else:
            print("Opción no válida. Seleccione 1, 2 o 3.")

# Llamada a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
