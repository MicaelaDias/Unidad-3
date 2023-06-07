from Personal import Personal
class Docente(Personal):
    __carrera=''
    __cargo=''
    __catedra=''
    __porcentaje=0

    def __init__(self, cuil='', apellido='', nombre='', sueldo=0, antiguedad=0,carrera='',cargo='',catedra='',area='',tipo='',porcentaje=0):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
        self.__porcentaje=porcentaje
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def setPorcentaje(self,porcentaje):
        self.__porcentaje=porcentaje
    
    def calcularSueldo(self):
        sueldoDocente=0.0
        
        if self.__cargo=='simple':
            self.__porcentaje+=10
        elif self.__cargo=='semiexclusivo':
            self.__porcentaje+=20

        elif self.__cargo=='exclusivo':
            self.__porcentaje+=50
        porCargo=(self.getSueldo()*self.__porcentaje)/100
        sueldoDocente=self.getSueldo()+self.antiguedad()+porCargo
        return sueldoDocente
        
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),carrera=self.__carrera,cargo=self.__cargo,catedra=self.__catedra)
        )
        return d