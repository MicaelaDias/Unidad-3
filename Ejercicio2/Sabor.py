class Sabor:
    __idSabor=0
    __cantidad=0
    __ingredientes=''
    __nombreSabor=''
    __cantidadP=0

    @classmethod
    def getId(cls):
        cls.__cantidad+=1
        return cls.__cantidad

    def __init__(self,ingredientes='',nombre='',cantidadP=0):
        self.__idSabor=self.getId()
        self.__ingredientes=ingredientes
        self.__nombreSabor=nombre   
        self.__cantidadP=cantidadP
    def __str__(self):
        return '{}, {}'.format(self.__idSabor,self.__nombreSabor)
    def getNombre(self):
        return self.__nombreSabor
    def getIdSabor(self):
        return self.__idSabor
    def setCantidad(self,cantidad):
        self.__cantidadP=cantidad
    def getCantidad(self):
        return self.__cantidadP
    def __gt__(self,otro):
        bandera=False
        if self.__cantidadP<otro.getCantidad():
            bandera=True
        return bandera