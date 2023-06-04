from Carrera import  Carrera
from Facultad import Facultad
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir
            }
    def lanzarMenu(self,manejador):
        #Menu opciones
        
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1: mostrar facultad y sus carreras.')
            print('-Ingrese 2: mostrar codigo de carrera, facultad y localidad.')
            print('-Ingrese 3: para funcion Test.')
            print('-Ingrese 4: para salir.')
            
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion == '1'  or opcion=='2'or opcion=='3':
                ejecutar(manejador)      
            else:
                ejecutar()
    def opcion1(self,manejador):
        codigo=int(input('Ingrese el codigo de facultad:'))
        manejador.buscarFacultad(codigo)
        
    def opcion2(self,manejador):
        nombre=input('Ingresar el nombre de una carrera: ')
        manejador.buscarCarrera(nombre)
    def opcion3(self,manejador):
        manejador.funcionTest()
        carrera=Carrera()
        facultad=Facultad()
        carrera.funcionTest()
        facultad.funcionTest()

    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')