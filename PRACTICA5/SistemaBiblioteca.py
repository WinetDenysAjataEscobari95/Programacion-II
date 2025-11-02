from datetime import date, timedelta

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []     
        self.autores = []    
        self.prestamos = []   
        # COMPOSICIÓN: Horario como clase interna
        self.horario = self.Horario("Lunes a Viernes", "08:00", "18:00")
    
    # CLASE INTERNA Horario (Composición)
    class Horario:
        def __init__(self, dias_apertura, hora_apertura, hora_cierre):
            self.dias_apertura = dias_apertura
            self.hora_apertura = hora_apertura
            self.hora_cierre = hora_cierre

        def mostrarHorario(self):
            print(f"Horario: {self.dias_apertura}, de {self.hora_apertura} a {self.hora_cierre}")

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarAutor(self, autor):
        self.autores.append(autor)

    def prestarLibro(self, estudiante, libro):
        if libro in self.libros:
            prestamo = Prestamo(estudiante, libro)
            self.prestamos.append(prestamo)
            print(f"✅ Se realizó el préstamo del libro '{libro.titulo}' a {estudiante.nombre}")
        else:
            print(f"❌ El libro '{libro.titulo}' no está disponible")

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

        print("\nHorario de atención:")
        self.horario.mostrarHorario()

    def cerrarBiblioteca(self):
        print(f"\n🔒 La biblioteca '{self.nombre}' está cerrando...")
        self.prestamos.clear()
        print("Todos los préstamos han sido eliminados.")


class Libro:
    def __init__(self, titulo, isbn, contenidos_paginas):
        self.titulo = titulo
        self.isbn = isbn
        # COMPOSICIÓN: Páginas como clases internas
        self.paginas = [self.Pagina(i+1, contenido) for i, contenido in enumerate(contenidos_paginas)]
    
    # CLASE INTERNA Pagina (Composición)
    class Pagina:
        def __init__(self, numero, contenido):
            self.numero = numero
            self.contenido = contenido

        def mostrarPagina(self):
            print(f"Página {self.numero}: {self.contenido}")

    def leer(self):
        print(f"--- Leyendo '{self.titulo}' ---")
        for pagina in self.paginas:
            pagina.mostrarPagina()


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.nombre} ({self.nacionalidad})")


class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} - Código: {self.codigo}")


class Prestamo:
    def __init__(self, estudiante, libro):
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=15)  # 15 días para devolución
        self.estudiante = estudiante  # ASOCIACIÓN
        self.libro = libro  # ASOCIACIÓN

    def mostrarInfo(self):
        print(f"Préstamo: Libro '{self.libro.titulo}' a {self.estudiante.nombre}")
        print(f"  Fecha préstamo: {self.fecha_prestamo}")
        print(f"  Fecha devolución: {self.fecha_devolucion}")


# PRUEBA MEJORADA QUE DEMUESTRA LAS TRES RELACIONES
if __name__ == "__main__":
    print("=== DEMOSTRACIÓN DE RELACIONES ===")
    
    # 1. DEMOSTRAR AGREGACIÓN (los objetos existen independientemente)
    print("\n1. RELACIÓN DE AGREGACIÓN:")
    autor = Autor("Mario Vargas Llosa", "Peruana")
    libro = Libro("La ciudad y los perros", "ISBN003", ["Capítulo 1", "Capítulo 2"])
    
    print(" - Autor y Libro creados independientemente")
    autor.mostrarInfo()
    print(f" - Libro: {libro.titulo}")
    
    biblioteca = Biblioteca("Biblioteca Central UMSA")
    
    # AGREGACIÓN: Los libros y autores existen fuera de la biblioteca
    biblioteca.agregarAutor(autor)
    biblioteca.agregarLibro(libro)
    print(" - Autor y Libro agregados a la biblioteca (Agregación)")
    
    # 2. DEMOSTRAR COMPOSICIÓN (los objetos no existen independientemente)
    print("\n2. RELACIÓN DE COMPOSICIÓN:")
    print(" - Horario creado automáticamente con la Biblioteca")
    biblioteca.horario.mostrarHorario()
    
    libro_composicion = Libro("Composición Demo", "ISBN004", ["Pág1", "Pág2"])
    print(" - Páginas creadas automáticamente con el Libro")
    libro_composicion.leer()
    
    # 3. DEMOSTRAR ASOCIACIÓN (uso temporal entre objetos independientes)
    print("\n3. RELACIÓN DE ASOCIACIÓN:")
    estudiante = Estudiante("202502", "Carlos Pérez")
    estudiante.mostrarInfo()
    
    # ASOCIACIÓN: Préstamo conecta Estudiante y Libro temporalmente
    prestamo = Prestamo(estudiante, libro)
    prestamo.mostrarInfo()
    print(" - Préstamo asocia Estudiante y Libro (Asociación)")
    
    # Estado final
    print("\n" + "="*50)
    biblioteca.mostrarEstado()
    
    # Cerrar biblioteca
    biblioteca.cerrarBiblioteca()