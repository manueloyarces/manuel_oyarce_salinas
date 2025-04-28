def calcular_volumen_esfera(radio):
    pi = 3.1416  # La Constante de pi
    volumen = (4 / 3) * pi * (radio ** 3)  # Fórmula de Volumen
    return volumen

# Ejemplo de su uso
radio_esfera = 7  # Argumento
volumen_calculado = calcular_volumen_esfera(radio_esfera)  # Llamada a la función
print(f"El volumen de la esfera con radio {radio_esfera} es: {volumen_calculado}")
