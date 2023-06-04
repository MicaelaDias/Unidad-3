from Helado import Helado
class ListaHelados:
    __listaHelados=[]

    def __init__(self):
        self.__listaHelados=[]
    def agregarHelados(self,helado):
        if type(helado)==Helado:
            self.__listaHelados.append(helado)
        else:
            print('No se puede agregar.')
    
    def saboresMasPedidos(self):
        max = 0
        indice = 0
        for i in range(len(self.__listaHelados)):
           
            cantidad= self.__listaHelados[i].contarSabores(indice+1)
            if cantidad>max:
                max = cantidad
        return max
    def verificarSabor(self,sabor):
        cantidad=0.0
        for i in range(len(self.__listaHelados)):
            if self.__listaHelados[i].buscarSabor(sabor)!= None:
                cantidad += self.__listaHelados[i].contarGramos()
        print('cantidad de gramos {}'.format(cantidad))
   
    def verificarSabores(self,tipo):
        for i in range(len(self.__listaHelados)):
            if self.__listaHelados[i].buscarTipo(tipo):
                self.__listaHelados[i].mostrarSabores()
    def calcularImporte(self):
        tipoUno=0.0
        tipoDos=0.0
        tipoTres=0.0
        tipoCuatro=0.0
        tipoCinco=0.0
        total=0.0
        for i in range(len(self.__listaHelados)):
            if self.__listaHelados[i].getGramos()==float(100):
                tipoUno+=self.__listaHelados[i].getPrecio()
            elif self.__listaHelados[i].getGramos()==float(150):
                tipoDos+=self.__listaHelados[i].getPrecio()
            elif self.__listaHelados[i].getGramos()==float(250):
                tipoTres+=self.__listaHelados[i].getPrecio()
            elif self.__listaHelados[i].getGramos()==float(500):
                tipoCuatro+=self.__listaHelados[i].getPrecio()
            elif self.__listaHelados[i].getGramos()==float(1000):
                tipoCinco+=self.__listaHelados[i].getPrecio()
        total=tipoUno+tipoDos+tipoTres+tipoCuatro+tipoCinco
        print('Total de helados vendidos de 100 gramos:{}'.format(tipoUno))
        print('Total de helados vendidos de 150 gramos:{}'.format(tipoDos))
        print('Total de helados vendidos de 250 gramos:{}'.format(tipoTres))
        print('Total de helados vendidos de 500 gramos:{}'.format(tipoCuatro))
        print('Total de helados vendidos de 1000 gramos:{}'.format(tipoCinco))
        print('Total recaudado:{}'.format(total))
    def mostrarCinco(self,manejaSabores):
        cantidadMax=self.saboresMasPedidos()
        manejaSabores.saboresMasVendidos(cantidadMax)