from Helado import Helado
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
    def lanzarMenu(self,manejaHelados,manejaSabores):
        
       
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1: para registrar pedidos .')
            print('-Ingrese 2:para mostrar 5 sabores mas vendidos.')
            print('-Ingrese 3 :para saber la cantidad de gramos.')
            print('-Ingrese 4: para mostrar sabores vendidos .')
            print('-Ingrese 5: mostrar importe total de la heladeria y por cada tipo de helado.')
            print('-Ingrese 6: para salir.')
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if (opcion=='1' or opcion=='2'):
                ejecutar(manejaHelados,manejaSabores)
            elif opcion=='3' or opcion=='4' or opcion=='5':
                ejecutar(manejaHelados)
                
            else:
                ejecutar()
    def opcion1(self,manejaHelados,manejaSabores):
        print('*******Registrar Pedido***********')
        peso=float(input('Ingrese el peso del helado (100gr,150gr,250gr,500gr,1000gr)'))
        precio=float(input('Ingrese el precio del helado:'))
        helado=Helado(peso,precio)
        
        bandera = True
        while bandera:
            manejaSabores.mostrarSabores()
            opcion=input('Ingrese el numero del sabor o f para finalizar:')
            if opcion=='f':
                bandera = False
            else:
                try:
                    opcion=int(opcion)
                except ValueError:
                    print('Debe ingresar un numero entero.')
                else:
                    
                    sabor=manejaSabores.buscarSabor(opcion)
                    helado.agregarSabor(sabor) 
        manejaHelados.agregarHelados(helado)
        
    def opcion2(self,manejaHelados,manejaSabores):
        manejaHelados.mostrarCinco(manejaSabores)
        
    def opcion3(self,manejaHelados):
        sabor=int(input('Ingrese el numero de sabor:'))
        manejaHelados.verificarSabor(sabor)
    def opcion4(self,manejaHelados):
        tipo=float(input('Ingrese el tipo de helado(100gr,150gr,250gr,500gr,1000gr):'))
        manejaHelados.verificarSabores(tipo)
        
    def opcion5(self,manejaHelados):
        manejaHelados.calcularImporte()
    def salir(self):
        print('Se cerro el menu.')
    def error(self):
        print('Opcion incorrecta.')