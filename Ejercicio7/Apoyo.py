from Personal import Personal
class Apoyo(Personal):
    __categoria=0
    
    def __init__(self, cuil='', apellido='', nombre='', sueldo=0, antiguedad=0,carrera='',cargo='',catedra='',area='',tipo='',categoria=0):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad,carrera,cargo,catedra,area,tipo)
        self.__categoria=categoria
    def calcularSueldo(self):
        sueldoPesonalApoyo=0.0
        porcentaje=0
        porCategoria=0.0
        if self.__categoria>=1 and self.__categoria<=10:
            porcentaje+=10
        elif self.__categoria>=11 and self.__categoria<=20:
            porcentaje+=20
        elif self.__categoria==21 or self.__categoria==22:
            porcentaje+=30

        porCategoria=(self.getSueldo()*porcentaje)/100
        sueldoPesonalApoyo=self.getSueldo()+self.antiguedad()+porCategoria
        return sueldoPesonalApoyo

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),categoria=self.__categoria)
        )
        return d