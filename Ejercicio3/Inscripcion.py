from Persona import Persona
class Inscripcion:
    __fecha=None
    __pago=None
    __persona=None
    __taller=None

    def __init__(self,fecha=None,pago=False,persona=None,taller=None):
        self.__fecha=fecha
        self.__pago=pago
        if type(persona)==Persona:
            self.__persona=persona
       
        self.__taller=taller
    def buscarDni(self,dni):
        bandera=False
        if self.__persona.getDni()==dni:
            bandera=True
        return bandera
    def getFecha(self):
        return self.__fecha
    def getPago(self):
        return self.__pago
    def mostrarDatos(self):
        print('Nombre y Apellido:{}, Direccion:{},DNI:{}'.format(self.__persona.getNombre(),self.__persona.getDireccion(),self.__persona.getDni()))
    def setPago(self,estado):
        self.__pago=estado
    def guardar(self,write):
        write.writerow([self.__persona.getDni(),self.__taller.getId(),self.__fecha.strftime('%Y/%m/%d'),self.__pago])