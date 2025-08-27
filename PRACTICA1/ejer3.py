import math

class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros

    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def desviacion(self):
        prom = self.promedio()
        suma = sum((x - prom)**2 for x in self.numeros)
        return math.sqrt(suma / (len(self.numeros) - 1))


# Programa de prueba
numeros = [float(x) for x in input("Ingrese 10 números: ").split()]
est = Estadistica(numeros)

print("El promedio es", round(est.promedio(), 2))
print("La desviación estándar es", round(est.desviacion(), 5))