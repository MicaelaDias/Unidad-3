class MenuDirector:
    __opciones={}

    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.salir
        }
    def lanzarMenu(self,lista):
        i=len(self.__opciones)
        opcion=0
        while i!=opcion:
            print('Ingrese 1: para modificar sueldo basico')
            print('Ingrese 2:para modificar porcentaje por cargo')
            print('Ingrese 3: para modificar porcentaje por categoria')
            print('Ingrese 4: para modificar importe extra ')
            print('Ingrese 5: para salir')
            opcion=self.cargarNumeroEntero('Ingrese la opcion:')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>=1 and opcion<5:
                ejecutar(lista)
            else:
                ejecutar()
    def opcion1(self,lista):
        dni=input('Ingrese el dni:')
        sueldo=float(input('Ingrese el sueldo:'))
        lista.modificarBasico(dni,sueldo)

    def opcion2(self,lista):
        dni=input('Ingrese el dni:')
        porcentaje=self.cargarNumeroEntero('Ingrese el procentaje')
        lista.modificarPorcentajeporcargo(dni,porcentaje)

    def opcion3(self,lista):
        dni=input('Ingrese el dni:')
        porcentaje=self.cargarNumeroEntero('Ingrese el procentaje')
        lista.modificarPorcentajeporcategoría(dni,porcentaje)
       
    def opcion4(self,lista):
        dni=input('Ingrese el dni:')
        importe=float(input('Ingrese el importe:'))
        lista.modificarImporteExtra(dni,importe)
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def error(self):
        print('Opcion Incorrecta')
    def salir(self):
        print('Se cerro el menu')