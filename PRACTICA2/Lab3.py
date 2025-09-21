import random

# Clase base
class Juego:
    def __init__(self, numero_de_vidas):
        self.numero_de_vidas = numero_de_vidas
        self.record = 0

    def reinicia_partida(self, vidas):
        self.numero_de_vidas = vidas

    def actualiza_record(self):
        self.record += 1
        print(f"Nuevo record: {self.record}")

    def quita_vida(self):
        self.numero_de_vidas -= 1
        if self.numero_de_vidas > 0:
            print(f"Te quedan {self.numero_de_vidas} vidas.")
            return True
        else:
            print("No te quedan más vidas.")
            return False


# Juego base de adivinanza
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas):
        super().__init__(vidas)
        self.numero_a_adivinar = None

    def valida_numero(self, n):
        return 0 <= n <= 10

    def juega(self):
        self.reinicia_partida(3)
        self.numero_a_adivinar = random.randint(0, 10)

        print("Adivina un número entre 0 y 10:")

        while True:
            try:
                intento = int(input("Ingresa tu número: "))
            except ValueError:
                print("Debes ingresar un número entero.")
                continue

            if not self.valida_numero(intento):
                print("Número inválido. Intenta de nuevo.")
                continue

            if intento == self.numero_a_adivinar:
                print("¡Acertaste!")
                self.actualiza_record()
                break
            else:
                if self.quita_vida():
                    if intento < self.numero_a_adivinar:
                        print("El número a adivinar es MAYOR.")
                    else:
                        print("El número a adivinar es MENOR.")
                else:
                    print(f"Perdiste. El número era: {self.numero_a_adivinar}")
                    break


# Juego de adivinar pares
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def valida_numero(self, n):
        if n < 0 or n > 10:
            print("Número fuera de rango (0-10).")
            return False
        if n % 2 != 0:
            print("El número debe ser PAR.")
            return False
        return True


# Juego de adivinar impares
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def valida_numero(self, n):
        if n < 0 or n > 10:
            print("Número fuera de rango (0-10).")
            return False
        if n % 2 == 0:
            print("El número debe ser IMPAR.")
            return False
        return True


# Clase principal
if __name__ == "__main__":
    juego1 = JuegoAdivinaNumero(3)
    juego2 = JuegoAdivinaPar(3)
    juego3 = JuegoAdivinaImpar(3)

    print("=== Juego Normal ===")
    juego1.juega()

    print("\n=== Juego Adivina Par ===")
    juego2.juega()

    print("\n=== Juego Adivina Impar ===")
    juego3.juega()
