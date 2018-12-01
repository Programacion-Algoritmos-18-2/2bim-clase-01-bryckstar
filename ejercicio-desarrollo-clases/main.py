from paquete_archivo.archivo import *
from paquete_modelado.modelo import *

ml = ArchivoLeer()
me = ArchivoEscribir()
lista = ml.obtener_informacion()
lista = [l.split("|") for l in lista]
lista = lista[1:]
for d in lista:
    p = Persona(d[0], d[1], d[2], d[3])
    print(p)
    me.agregar_informacion(p)

ml.cerrar_archivo()
me.cerrar_archivo()
