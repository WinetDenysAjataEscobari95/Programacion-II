import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminante(self):
        return self.b**2 - 4*self.a*self.c

    def getRaiz1(self):
        disc = self.getDiscriminante()
        return (-self.b + math.sqrt(disc)) / (2*self.a)

    def getRaiz2(self):
        disc = self.getDiscriminante()
        return (-self.b - math.sqrt(disc)) / (2*self.a)


# Programa de prueba
a, b, c = [float(x) for x in input("Ingrese a, b, c: ").split()]
ecuacion = EcuacionCuadratica(a, b, c)

d = ecuacion.getDiscriminante()

if d > 0:
    print("La ecuación tiene dos raíces:", ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())
elif d == 0:
    print("La ecuación tiene una raíz:", ecuacion.getRaiz1())
else:
    print("La ecuación no tiene raíces reales")