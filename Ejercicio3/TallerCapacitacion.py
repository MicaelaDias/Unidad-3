from Inscripcion import Inscripcion
class TallerCapacitacion:
    __idTaller=0
    __nombre=''
    __vacantes=0
    __montoI=0
    __inscripciones=None

    def __init__(self,idTaller=0,nombre='',vacantes=0,montoI=0):
        self.__idTaller=idTaller
        self.__nombre=nombre
        self.__vacantes=vacantes
        self.__montoI=montoI
        self.__inscripciones=[]
    def __str__(self):
        return '{},{},{}'.format(self.__idTaller,self.__nombre,self.__montoI)
    def getId(self):
        return self.__idTaller
    def descontar(self,cantidad):
        if cantidad<self.__vacantes:
            self.__vacantes-=cantidad
    def getNombre(self):
        return self.__nombre
    def getMonto(self):
        return self.__montoI
    def agregarInscripcion(self,inscripcion):
        if type(inscripcion)==Inscripcion:
            self.__inscripciones.append(inscripcion)
        else:
            print('no se puede agregar.')
    def inscribirPersona(self,persona,fecha,pago):
        res=None
        bandera=False
        if not bandera:
            inscripcion=Inscripcion(fecha,pago,persona,self)
            self.agregarInscripcion(inscripcion)
            bandera=True
            res=inscripcion
        return res
        
        

    def buscarInscripcion(self,dni):
        i = 0
        bandera = False
        indice=None
        while i<len(self.__inscripciones) and not bandera:
            if self.__inscripciones[i].buscarDni(dni):
                bandera = True
                indice = i
            else:
                i+=1
        return indice
    def buscarInscriptos(self):
        for i in range(len(self.__inscripciones)):
            self.__inscripciones[i].mostrarDatos()