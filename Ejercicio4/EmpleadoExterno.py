from Empleado import Empleado
class EmpleadoExterno(Empleado):
    
    __fechaI=None
    __fechaF=None
    __tarea=''
    __montoViatico=0.0
    __costoDeObra=0.0
    __montoSeguro=0.0

    def __init__(self, dni='',nombre='', direccion='', telefono='',fechaI=None,fechaF=None,tarea='',montoViatico=0.0,costo=0.0,montoSeguro=0.0):
        super().__init__(dni,nombre, direccion, telefono)
       
        self.__fechaI=fechaI
        self.__fechaF=fechaF
        self.__tarea=tarea
        self.__montoViatico=montoViatico
        self.__costoDeObra=costo
        self.__montoSeguro=montoSeguro
    def sueldo(self):
        sueldo=0.0
        sueldo=self.__costoDeObra-self.__montoViatico-self.__montoSeguro
        return sueldo
    def getCosto(self):
        return self.__costoDeObra
    def getTarea(self):
        return self.__tarea
    def getFecha(self):
        return self.__fechaF
        
        