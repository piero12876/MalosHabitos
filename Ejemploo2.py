def calcular(multiplicando, multiplicador, sumando):
    res = multiplicando * multiplicador + sumando
    return res

def principal():
    multiplicando = float(input("Multiplicando: "))
    multiplicador = float(input("Multiplicador: "))
    sumando = float(input("Sumando: "))
    resultado = calcular(multiplicando, multiplicador, sumando)
    print("El resultado es:", resultado)

principal()
