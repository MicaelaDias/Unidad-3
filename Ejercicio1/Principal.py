from ManejadorFacultades import ManejadorFacultades
from Menu import Menu
if __name__=='__main__':
    manejador=ManejadorFacultades()
    manejador.cargarArchivo()
    menu=Menu()
    menu.lanzarMenu(manejador)