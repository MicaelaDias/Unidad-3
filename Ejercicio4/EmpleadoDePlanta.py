from Empleado import Empleado
class EmpleadoDePlanta(Empleado):
    __sueldoBasico=0.0
    __antiguedad=0

    def __init__(self, dni='',nombre='', direccion='', telefono='',sueldoBasico=0.0,antiguedad=0):
        super().__init__(dni,nombre, direccion, telefono)
        self.__sueldoBasico=sueldoBasico
        self.__antiguedad=antiguedad
    def sueldo(self):
        sueldo=0.0
        sueldo=self.__sueldoBasico + (self.__sueldoBasico * 0.01) * self.__antiguedad
        return sueldo