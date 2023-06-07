from Docente import Docente
from Investigador import Investigador

class DocenteInvestigador(Docente,Investigador):
    __catgeoriaI=''
    __importeExtra=0.0
    def  __init__(self, cuil='', apellido='', nombre='', sueldo=0.0, antiguedad=0, carrera='', cargo='', catedra='', area='',tipo='',cat='',importe=0.0):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__catgeoriaI=cat
        self.__importeExtra=importe
    def calcularSueldo(self):
        sueldoDocenteInvestigador=0.0
        sueldoDocenteInvestigador=Docente.calcularSueldo(self)+self.__importeExtra
        return sueldoDocenteInvestigador
    def getCategoria(self):
        return self.__catgeoriaI
    def getImporteE(self):
        return self.__importeExtra
    def setImporte(self,importe):
        self.__importeExtra=importe
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(cuil=self.getCuil(),apellido=self.getApellido(),nombre=self.getNombre(),sueldoBasico=self.getSueldo(),
            antiguedad=self.getAntiguedad(),carrera=self.getCarrera(),cargo=self.getCargo(),catedra=self.getCatedra(),areaInvestigacion=self.getArea(),tipoInvestigacion=self.getTipo(),
            categoriaE=self.__catgeoriaI,importe=self.__importeExtra)
        )
        return d