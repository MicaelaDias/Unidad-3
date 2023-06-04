from Empleado import Empleado

class EmpleadoContratado(Empleado):
    __fechaI=None
    __fechaF=None
    __cantidadH=0
    __valorHora=0.0

    @classmethod
    def setValor(cls,valor):
        cls.__valorHora=valor
    @classmethod
    def getValor(cls):
        return cls.__valorHora
    def __init__(self, dni='', nombre='',direccion='', telefono='',fechaI=None,fechaF=None,cantidadH=0):
        super().__init__(dni,nombre, direccion, telefono)
        self.__fechaI=fechaI
        self.__fechaF=fechaF
        self.__cantidadH=cantidadH    
    def acumularHoras(self,cantidad):
        if type(cantidad)==int:
            self.__cantidadH+=cantidad
    def getCantidad(self):
        return self.__cantidadH
    def sueldo(self):
        sueldo=0.0
        sueldo = self.__cantidadH*self.__valorHora
        return sueldo