from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario_mensual(self) -> float:
        pass

    def __str__(self):
        return f"Empleado: {self.nombre}"


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salario_anual: float):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def calcular_salario_mensual(self) -> float:
        return self.salario_anual / 12

    def __str__(self):
        return f"{super().__str__()}, Salario anual: {self.salario_anual}"


class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre: str, horas_trabajadas: float, tarifa_hora: float):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_salario_mensual(self) -> float:
        return self.horas_trabajadas * self.tarifa_hora

    def __str__(self):
        return f"{super().__str__()}, Horas: {self.horas_trabajadas}, Tarifa: {self.tarifa_hora}"


# Programa de prueba
if __name__ == "__main__":
    empleados = []

    print("=== Ingreso de empleados a tiempo completo ===")
    for i in range(3):
        nombre = input("Nombre: ")
        salario = float(input("Salario anual: "))
        empleados.append(EmpleadoTiempoCompleto(nombre, salario))

    print("\n=== Ingreso de empleados por horas ===")
    for i in range(2):
        nombre = input("Nombre: ")
        horas = float(input("Horas trabajadas: "))
        tarifa = float(input("Tarifa por hora: "))
        empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))

    print("\n=== Lista de empleados ===")
    for e in empleados:
        print(f"{e.nombre} -> Salario mensual: {e.calcular_salario_mensual():.2f}")
