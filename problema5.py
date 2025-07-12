class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None

    def display(self):
        print("Nombre:", self.nombre)
        print("Registro:", self.registro)
        print("Edad:", self.edad if self.edad is not None else "No asignada")
        print("Nota:", self.nota if self.nota is not None else "No asignada")

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.nota = nota

alumno1 = Alumno("Carlos Sánchez", "20254001")

alumno1.setAge(21)
alumno1.setNota(18)

alumno1.display()