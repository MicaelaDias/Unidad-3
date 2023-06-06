from Personal import Personal
class Investigador(Personal):
    __area=''
    __tipo=''

    def __init__(self, cuil='', apellido='', nombre='', sueldo=0, antiguedad=0,carrera='',cargo='',catedra='',area='',tipo=''):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad,carrera,cargo,catedra,area,tipo)
        self.__area=area
        self.__tipo=tipo
    def getArea(self):
        return self.__area
    def getTipo(self):
        return self.__tipo
    def calcularSueldo(self):
        sueldoInvestigador=0.0
        sueldoInvestigador=self.getSueldo()+self.antiguedad()
        return sueldoInvestigador
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),areaInvestigacion=self.__area,tipoInvestigacion=self.__tipo)
        )
        return d    