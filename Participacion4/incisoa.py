import math

class Circulo2D:
    def __init__(self, x=0, y=0, radio=1):
        self.x = x
        self.y = y
        self.radio = radio

    def get_area(self):
        return math.pi * self.radio ** 2

    def get_perimetro(self):
        return 2 * math.pi * self.radio

    def contiene_punto(self, x, y):
        distancia = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return distancia <= self.radio

    def contiene_circulo(self, otro):
        distancia = math.sqrt((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2)
        return distancia + otro.radio <= self.radio

    def sobrepone(self, otro):
        distancia = math.sqrt((self.x - otro.x) ** 2 + (self.y - otro.y) ** 2)
        return distancia <= self.radio + otro.radio and distancia >= abs(self.radio - otro.radio)

if __name__ == "__main__":
    c1 = Circulo2D(2, 0, 1)

    print("Área:", c1.get_area())
    print("Perímetro:", c1.get_perimetro())
    print("c1 contiene el punto (2.5, 0)?", c1.contiene_punto(2.5, 0))
    print("c1 contiene el círculo (2,0,0.5)?", c1.contiene_circulo(Circulo2D(2, 0, 0.5)))
    print("c1 se sobrepone con el círculo (0,0,2)?", c1.sobrepone(Circulo2D(0, 0, 2)))