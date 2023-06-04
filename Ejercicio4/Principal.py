from ManejadorEmplados import ArregloEmpleados
from Menu import Menu
if __name__=='__main__':
    bandera=True
    while bandera:
        try:
            cantidad=int(input('Ingrese la cantidad de empleados'))
        except ValueError:
            print('Debe ingresar un numero')
        else:
            bandera=False
    manejador=ArregloEmpleados(cantidad)
    manejador.cargarArchivo()
    menu=Menu()
    menu.lanzarMenu(manejador)