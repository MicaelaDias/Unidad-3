import abc
from abc import ABC

class Empleado(ABC):
    __dni=''
    __nombre=''
    __direccion=''
    __telefono=''

    def __init__(self,dni='',nombre='',direccion='',telefono=''):
        self.__dni=dni
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
    def verificarDni(self,dni):
        bandera=False
        if self.__dni==dni:
            bandera=True
        return bandera
    @abc.abstractclassmethod
    def sueldo(self):
        pass
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getDni(self):
        return self.__dni
    def getTelefono(self):
        return self.__telefono