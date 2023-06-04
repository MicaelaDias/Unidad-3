from ManejadorInscripciones import ManejadorInscripciones
from ManejadorPersona import ListaPersona
from ManejadorTaller import ArregloTaller
from Menu import Menu

if __name__=='__main__':
    manejadorInscripciones=ManejadorInscripciones()
    manejadorPersona=ListaPersona()
    manejadorTaller=ArregloTaller()
    manejadorTaller.cargarArchivo()
    menu=Menu()
    menu.lanzarMenu(manejadorInscripciones,manejadorPersona,manejadorTaller)