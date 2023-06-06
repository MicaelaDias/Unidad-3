import abc
from abc import ABC

class Personal(ABC):
    __cuil=''
    __apellido=''
    __nombre=''
    __sueldo=0.0 
    __antiguedad=0

    def __init__(self,cuil='',apellido='',nombre='',sueldo=0.0,antiguedad=0,carrera='',cargo='',catedra='',area='',tipo=''):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldo=sueldo
        self.__antiguedad=antiguedad
    def getNombre(self):
        return self.__nombre
    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getSueldo(self):
        return self.__sueldo
    def getAntiguedad(self):
        return self.__antiguedad
    @abc.abstractclassmethod
    def calcularSueldo(self):
        pass
    def antiguedad(self):
        antiguedad=0
        antiguedad=(self.__sueldo*self.__antiguedad)/100
        return antiguedad
    def toJSON(self):
        return dict(cuil=self.__cuil,apellido=self.__apellido,nombre=self.__nombre,sueldoBasico=self.__sueldo,antiguedad=self.__antiguedad)