import csv
from Persona import Persona
class ListaPersona:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def agregarElemento(self,persona):
        if type(persona)==Persona:
            self.__lista.append(persona)
        else:
            print('No se puede agregar.')
    def buscarDni(self,dni):
        i = 0
        bandera = False
        indice=None
        while i<len(self.__lista) and not bandera:
            if self.__lista[i].getDni()==dni:
                bandera = True
                indice=i
            else:
                i+=1
        return indice
    def mostrarDatos(self):
        for i in range(len(self.__lista)):
            print('nombre{}'.format(self.__lista[i].getNombre()))
    def registrarPago(self,dni,manejadorI):
        indice=self.buscarDni(dni)
        if indice!=None:
            bandera=manejadorI.registrarPago(dni)
            if bandera:
                print('se registro el pago')