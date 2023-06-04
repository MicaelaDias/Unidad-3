from Sabor import Sabor
class Helado:
    __gramos=0.0
    __precio=0.0
    __sabores=[]

    def __init__(self,gramos=0.0,precio=0.0):
        self.__gramos=gramos
        self.__precio=precio
        self.__sabores=[]
        
    def agregarSabor(self,sabor):
        if type(sabor)==Sabor:
            
            self.__sabores.append(sabor)
        else:
            print('No se puede agregar.')
    def mostrarSabores(self):
       
        for i in range (len (self.__sabores)):
            print('{}'.format(self.__sabores[i].getNombre()))
    def getPrecio(self):
        return self.__precio
    def getGramos(self):
        return self.__gramos
    def contarSabores(self,numero):
        
        contar=0
        #cantidad=0
        for i in range(len(self.__sabores)):
            if self.__sabores[i].getIdSabor()==numero:
                contar += 1
        return contar
    def contarGramos(self):
        contar = 0
        resultado = 0.0
        for i in range(len(self.__sabores)):
            contar += 1
        resultado = self.__gramos/contar
        return resultado
    def buscarSabor(self,sabor):
        i = 0
        bandera = False
        indice = None
        while i<len(self.__sabores) and not bandera:
            if self.__sabores[i].getIdSabor()==sabor:
                bandera = True
                indice = i
            else:
                i+=1
        return indice
    def mostrarSabor(self,sabor):
        print(self.__sabores[sabor])
    def buscarTipo(self,tipo):
        bandera = False
        if self.__gramos==tipo:
            bandera = True
        return bandera