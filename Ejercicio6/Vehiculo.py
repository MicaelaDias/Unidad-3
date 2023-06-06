import  abc
from abc import ABC
class Vehiculo(ABC):
    __modelo=''
    __cantidadPuertas=0
    __color=''
    __precio=0.0

    def __init__(self,modelo='',cantidad=0,color='',precio=0.0):
        self.__modelo=modelo
        self.__cantidadPuertas=cantidad
        self.__color=color
        self.__precio=precio
    def toJSON(self):
        d=dict(
            modelo=self.__modelo,cantidad=self.__cantidadPuertas,color=self.__color,precio=self.__precio
        )
        return d
    def setPrecio(self,precio):
        self.__precio=precio
    def getPrecio(self):
        return self.__precio
    def getCantidad(self):
        return self.__cantidadPuertas
    def getColor(self):
        return self.__color
    def getModelo(self):
        return self.__modelo
    @abc.abstractclassmethod
    def importeVenta(self):
        pass
