from Vehiculo import Vehiculo
from VehiculoNuevo import VehiculoNuevo
from VehiculoUsado import VehiculoUsado
class Menu:
    __opciones={}

    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '6':self.opcion6,
            '7':self.opcion7,
            '8':self.salir
        }
    
    def lanzarMenu(self,lista,objectEncoder):
        i=str(self.__opciones)
        opcion=0
        while i!=opcion:
            print('*******Menu**********')
            print('Ingrese 1: insertar un vehiculo.')
            print('Ingrese 2: agregar un vehiculo.')
            print('Ingrese 3: mostrar un vehiculo.')
            print('Ingrese 4: modificar precio base.')
            print('Ingrese 5: mostrar el vehiculo mas economico.')
            print('Ingrese 6 para mostrar vehiculos a la venta.')
            print('Ingrese 7: para almacenar los datos en un archivo JSON')
            print('Ingrese 8: para salir')
            opcion=input('Ingrese una opcion:')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion=='1' or opcion=='2' or opcion=='3'or opcion=='4' or opcion=='5' or opcion=='6':
                ejecutar(lista)
            elif opcion=='7':
                ejecutar(lista,objectEncoder)
            else:
                ejecutar()
    def opcion1(self,lista):
        posicion=self.cargarNumero('Ingresar la posicion:')
        vehiculo=self.cargarVehiculo()
        lista.insertarElemento(vehiculo,posicion)

    def opcion2(self,lista):
        vehiculo=self.cargarVehiculo()
        lista.agregarElemento(vehiculo)
    def opcion3(self,lista):
        pos=self.cargarNumero('Ingrese una posicion')
        lista.mostrarElemento(pos)
    def opcion4(self,lista):
        patente=input('Ingrese una patente:')
        precio=float(input('Ingrese el precio base:'))
        lista.buscarPatente(patente,precio)
    def opcion5(self,lista):
        lista.buscarMin()
    def opcion6(self,lista):
        lista.mostrarTodos()
    def opcion7(self,lista,objectEncoder):
        lista.guardarArchivo(objectEncoder)

    def cargarVehiculo(self):
        resultado=None
        print('********CARGAR VEHICULO************')
        opcion=self.cargarNumero('ingrese 1 para cargar un vehiculo nuevo, ingrese 2 para cargar vehiculo viejo')
        if opcion<3:
            if opcion==1:
                print('******Vehiculo Nuevo********')
                modelo=input('Ingrese el modelo:')
                cantidad=self.cargarNumero('Ingrese la cantidad de puertas:')
                color=input('Ingrese el color:')
                precio=float(input('Ingrese el precio:'))
                version=input('Ingrese version:')
                vehiculo=VehiculoNuevo(modelo,cantidad,color,precio,version)
            elif opcion==2:
                print('****Vehiculo Usado******')
                modelo=input('Ingrese el modelo:')
                cantidad=self.cargarNumero('Ingrese la cantidad de puertas:')
                color=input('Ingrese el color:')
                precio=float(input('Ingrese el precio:'))
                
                marca=input('Ingrese la marca:')
                patente=input('Ingrese la patente:')
                año=self.cargarNumero('Ingrese el año:')
                kilometraje=self.cargarNumero('Ingrese el km:')
                vehiculo=VehiculoUsado(modelo,cantidad,color,precio,marca,patente,año,kilometraje)
            resultado=vehiculo
            return resultado
        else:
            print('Numero incorrecto')
                    

    def cargarNumero(self, mensaje='Ingrese un numero:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('Debe Ingresar un entero')
            else:
                bandera = False
        return numero
    def salir(self):
        print('Se cerro el menu')
    def error(self):
        print('Opcion incorrecta')    