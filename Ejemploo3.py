# Función para calcular el área de un rectángulo
def f(a, b):
    result = a * b
    return result

# Función para calcular el área de un triángulo
def g(base, altura):
    resultado = 0.5 * base * altura
    return resultado

# Función principal
def main():
    largo = float(input("Largo: "))
    ancho = float(input("Ancho: "))
    rect_area = f(largo, ancho)
    print("Área del rectángulo:", rect_area)

    base = float(input("Base: "))
    altura = float(input("Altura: "))
    tri_area = g(base, altura)
    print("Área del triángulo:", tri_area)

main()
