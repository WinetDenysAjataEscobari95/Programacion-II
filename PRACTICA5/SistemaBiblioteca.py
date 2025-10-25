from datetime import date

class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrarPagina(self):
        print(f"Página {self.numero}: {self.contenido}")


# Clase Libro
class Libro:
    def __init__(self, titulo, isbn, contenidos_paginas):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [Pagina(i+1, contenido) for i, contenido in enumerate(contenidos_paginas)]

    def leer(self):
        print(f"--- Leyendo '{self.titulo}' ---")
        for pagina in self.paginas:
            pagina.mostrarPagina()


# Clase Autor (Agregación)
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.nombre} ({self.nacionalidad})")


# Clase Estudiante (Asociación)
class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} - Código: {self.codigo}")


# Clase Prestamo (Asociación)
class Prestamo:
    def __init__(self, estudiante, libro):
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        print(f"Préstamo: Libro '{self.libro.titulo}' a {self.estudiante.nombre} el {self.fecha_prestamo}")

    def devolver(self):
        self.fecha_devolucion = date.today()
        print(f"Libro '{self.libro.titulo}' devuelto el {self.fecha_devolucion}")


# Clase Horario (Composición con Biblioteca)

class Horario:
    def __init__(self, dias_apertura, hora_apertura, hora_cierre):
        self.dias_apertura = dias_apertura
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrarHorario(self):
        print(f"Horario: {self.dias_apertura}, de {self.hora_apertura} a {self.hora_cierre}")


# Clase Biblioteca (Principal)
class Biblioteca:
    def __init__(self, nombre, dias_apertura, hora_apertura, hora_cierre):
        self.nombre = nombre
        self.libros = []     
        self.autores = []    
        self.prestamos = []   
        self.horario = Horario(dias_apertura, hora_apertura, hora_cierre)  # Composición

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarAutor(self, autor):
        self.autores.append(autor)

    def prestarLibro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        print(f"✅ Se realizó el préstamo del libro '{libro.titulo}' a {estudiante.nombre}")

    def mostrarEstado(self):
        print(f"\n=== Estado de la Biblioteca '{self.nombre}' ===")
        print("Autores registrados:")
        for a in self.autores:
            a.mostrarInfo()

        print("\nLibros disponibles:")
        for l in self.libros:
            print(f"- {l.titulo} (ISBN: {l.isbn})")

        print("\nPréstamos activos:")
        for p in self.prestamos:
            p.mostrarInfo()

        print()
        self.horario.mostrarHorario()

    def cerrarBiblioteca(self):
        print(f"\n🔒 La biblioteca '{self.nombre}' está cerrando...")
        self.prestamos.clear()
        print("Todos los préstamos han sido eliminados.")


# PRUEBA DEL SISTEMA
if __name__ == "__main__":
    # Crear autores
    autor1 = Autor("Gabriel García Márquez", "Colombiana")
    autor2 = Autor("Julio Verne", "Francesa")

    # Crear libros (cada uno con páginas internas)
    libro1 = Libro("Cien años de soledad", "ISBN001", ["Inicio...", "Desarrollo...", "Final..."])
    libro2 = Libro("Viaje al centro de la Tierra", "ISBN002", ["Capítulo 1", "Capítulo 2", "Capítulo 3"])

    # Crear biblioteca
    biblioteca = Biblioteca("Biblioteca UMSA", "Lunes a Viernes", "08:00", "18:00")

    # Agregar autores y libros
    biblioteca.agregarAutor(autor1)
    biblioteca.agregarAutor(autor2)
    biblioteca.agregarLibro(libro1)
    biblioteca.agregarLibro(libro2)

    # Crear estudiante
    estudiante1 = Estudiante("202501", "Andrea Choque")

    # Realizar préstamo
    biblioteca.prestarLibro(estudiante1, libro1)

    # Mostrar estado general
    biblioteca.mostrarEstado()

    # Cerrar biblioteca
    biblioteca.cerrarBiblioteca()
