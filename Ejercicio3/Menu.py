from datetime import date
from Persona import Persona

class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.opcion5,
            '6':self.salir
            }
    def lanzarMenu(self,manejadorI,manejadorP,manejadorT):
        
       
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1: para registrar inscripcion .')
            print('-Ingrese 2: para consultar inscripcion')
            print('-Ingrese 3: para consultar inscriptos.')
            print('-Ingrese 4: registrar pago.')
            print('-Ingrese 5: guardar inscripciones.')
            print('-Ingrese 6: para salir.')
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if (opcion=='1' or opcion=='2'):
                ejecutar(manejadorI,manejadorP,manejadorT)
            elif opcion=='3':
                ejecutar(manejadorT)
            elif opcion=='4':
                ejecutar(manejadorP,manejadorI)
            elif opcion=='5':
                ejecutar(manejadorI)
            else:
                ejecutar()
    def opcion1(self,manejadorI,manejadorP,manejadorT):
        print('*****Inscripcion***')
        dni=input('Ingrese el DNI:')
        indice=manejadorP.buscarDni(dni)
        if indice==None:
            print('*****Datos de la persona*******')
            nombre=input('Ingrese su nombre y apellido:')
            direccion=input('Ingrese la direccion:')
            persona=Persona(nombre,direccion,dni)
            print('*******Datos del Taller*************')
            manejadorT.mostrar()
            id=self.cargarNumero('Ingrese el numero del taller:')
            pos=manejadorT.buscarTaller(id)
            if pos!=None:
                bandera=manejadorT.buscarInscripcion(dni,id)
                if not bandera:
                    print('****Fecha de Inscripcion****')
                    fecha=self.cargarFecha()
                    manejadorT.inscribirPersona(pos,persona,fecha,False,manejadorI,manejadorP)
                    



    def opcion2(self,manejadorI,manejadorP,manejadorT):
        dni=input('Ingrese el DNI a buscar:')
        manejadorT.buscarPersona(dni,manejadorI)        
    def opcion3(self,manejadorT):
        taller=self.cargarNumero('Ingrese el identificador de un taller:')
        manejadorT.mostrarInscriptos(taller)
    def opcion4(self,manejadorP,manejadorI):
        dni=input('Ingrese el dni:')
        manejadorP.registrarPago(dni,manejadorI)

        
    def opcion5(self,manejadorI):
        manejadorI.guardarInscripciones()
    def cargarNumero(self,mensaje='Ingrese un numero:'):
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
    def cargarFecha(self):
        fecha=None
        bandera=True
        while bandera:
            try:
                dia=int(input('Ingrese el dia:'))
                mes=int(input('Ingrese el mes:'))
                año=int(input('Ingrese el año:'))
                fecha=date(año,mes,dia)
            except ValueError:
                print('DEBE INGRESAR UN NUMERO ENTERO')
            else:
                bandera=False
        return fecha

    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')