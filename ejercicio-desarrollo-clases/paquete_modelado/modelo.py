class Persona(object):

    def __init__(self, n, nota1, nota2, nota3):
        self.nombre = n
        self.nota1 = int(nota1)
        self.nota2 = int(nota2)
        self.nota3 = int(nota3)

    def setNombre(self, n):
        self.nombre = n

    def setNota1(self, n):
        self.nota1 = n

    def setNota2(self, n):
        self.nota2 = n

    def setNota3(self, n):
        self.nota3 = n

    def getNombre(self):
        return self.nombre

    def getNota1(self):
        return self.nota1

    def getNota2(self):
        return self.nota2

    def getNota3(self):
        return self.nota3

    def promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def __str__(self):
        return "%s|%.2f\n" % (self.nombre, self.promedio())
