class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.salir,
            
            }
    def lanzarMenu(self,manejador):
        
       
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1: para registrar hora .')
            print('-Ingrese 2: total de tareas')
            print('-Ingrese 3: ayuda economica.')
            print('-Ingrese 4: calcular sueldo.')
            print('-Ingrese 5: salir.')
        
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if (opcion=='1' or opcion=='2' or opcion=='3'or opcion=='4'):
                ejecutar(manejador)
         
            
            else:
                ejecutar()
    def opcion1(self,manejador):
        dni=input('Ingrese el DNI a buscar:')
        cantidad=self.cargarNumero('Ingrese la cantidad de horas trabjadas:')
        manejador.incrementar(dni,cantidad)
    def opcion2(self,manejador):
        tarea=input('Ingrese una tarea:')
        manejador.mostrarMonto(tarea)
          
    def opcion3(self,manejador):
        manejador.listar()
    def opcion4(self,manejador):
        manejador.mostrarEmpleados()

        

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


    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')