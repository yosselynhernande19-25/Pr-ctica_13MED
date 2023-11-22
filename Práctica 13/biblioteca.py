class Biblioteca:
    def __init__(self):
        self.pila_libros_prestados = []

    def prestar_libro(self, libro):
        self.pila_libros_prestados.append(libro)
        print(f"Libro prestado: {libro}")

    def devolver_libro(self):
        if not self.pila_libros_prestados:
            print("No hay libros prestados actualmente.")
        else:
            libro_devuelto = self.pila_libros_prestados.pop()
            print(f"Libro devuelto: {libro_devuelto}")

    def mostrar_estado(self):
        if not self.pila_libros_prestados:
            print("La pila de libros prestados está vacía.")
        else:
            print("Libros prestados actualmente:")
            for libro in reversed(self.pila_libros_prestados):
                print(f"- {libro}")

# Crear una instancia de la clase Biblioteca
mi_biblioteca = Biblioteca()

# Realizar operaciones de préstamo y devolución con libros específicos
mi_biblioteca.prestar_libro("Cien años de soledad")
mi_biblioteca.prestar_libro("Don Quijote de la Mancha")

# Mostrar el estado de la pila después de préstamos
mi_biblioteca.mostrar_estado()

# Devolver un libro
mi_biblioteca.devolver_libro()

# Mostrar el estado de la pila después de la devolución
mi_biblioteca.mostrar_estado()


