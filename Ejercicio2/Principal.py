from ManejaHelados import ListaHelados
from ManejaSabores import ListaSabores
from Menu import Menu

if __name__=='__main__':
    manejaHelados=ListaHelados()
    manejaSabores=ListaSabores()
    menu=Menu()
    manejaSabores.cargarArchivo()
    menu.lanzarMenu(manejaHelados,manejaSabores)