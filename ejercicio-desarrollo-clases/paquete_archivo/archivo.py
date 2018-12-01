import codecs


class ArchivoLeer:

    def __init__(self):
        self.archivo = codecs.open("data/datos.csv", "r")

    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()


class ArchivoEscribir:
    def __init__(self):
        self.archivo = codecs.open("data/promedio.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s|%.2f\n" % (p.getNombre(), p.promedio()))

    def cerrar_archivo(self):
        self.archivo.close()
