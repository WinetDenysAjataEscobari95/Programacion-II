from abc import ABC, abstractmethod
import random

class Coloreado:
    def como_colorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color: str = "blanco"):
        self.color = color

    def set_color(self, color: str):
        self.color = color

    def get_color(self) -> str:
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass


class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str = "azul"):
        super().__init__(color)
        self.lado = lado

    def area(self) -> float:
        return self.lado * self.lado

    def perimetro(self) -> float:
        return 4 * self.lado

    def como_colorear(self) -> str:
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado de lado {self.lado}, {super().__str__()}"


class Circulo(Figura):
    def __init__(self, radio: float, color: str = "rojo"):
        super().__init__(color)
        self.radio = radio

    def area(self) -> float:
        return 3.1416 * (self.radio ** 2)

    def perimetro(self) -> float:
        return 2 * 3.1416 * self.radio

    def __str__(self):
        return f"Circulo de radio {self.radio}, {super().__str__()}"


# Programa de prueba
if __name__ == "__main__":
    figuras = []

    for i in range(5):
        tipo = random.randint(1, 2)  # 1=Cuadrado, 2=Circulo
        if tipo == 1:
            lado = random.randint(1, 10)
            figuras.append(Cuadrado(lado))
        else:
            radio = random.randint(1, 10)
            figuras.append(Circulo(radio))

    print("=== Lista de Figuras ===")
    for f in figuras:
        print(f"{f}")
        print(f"Área: {f.area():.2f}, Perímetro: {f.perimetro():.2f}")
        if isinstance(f, Coloreado):
            print(f.como_colorear())
        print("-" * 30)
