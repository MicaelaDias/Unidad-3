import csv
import numpy as np
from Inscripcion import Inscripcion
class ManejadorInscripciones:
    __cantidad=0
    __dimension=0
    __incremento=5
    __inscripciones=None

    def __init__(self,cantidad=0,dimension=0,incremento=5):
        self.__inscripciones=np.empty(dimension,dtype=Inscripcion)
        self.__cantidad=cantidad
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarElemento(self,inscripcion):
        if type(inscripcion)==Inscripcion:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__inscripciones.resize(self.__dimension)
            self.__inscripciones[self.__cantidad]=inscripcion
            self.__cantidad+=1
        else:
            print('no se puede agregar.')
    def mostrarInscripciones(self):
        for i in range(self.__cantidad):
            print('Inscripcion{}'.format(self.__inscripciones[i].getFecha()))
    def verificarEstado(self,dni):
        i = 0
        bandera=True
        resutado=None
        while i<self.__cantidad and bandera:
            if self.__inscripciones[i].buscarDni(dni):
                bandera=False
                resutado=self.__inscripciones[i].getPago()
            else:
                i+=1
        return resutado
    def registrarPago(self,dni):
        bandera=False
        for i in range(self.__cantidad):
            if self.__inscripciones[i].buscarDni(dni):
                self.__inscripciones[i].setPago(True)
                print('Estado de pago:{}'.format(self.__inscripciones[i].getPago()))
                bandera=True
        return bandera
    def guardarInscripciones(self):
        nombre='inscripciones.csv'
        archivo=open(nombre,'w',encoding='utf-8',newline='')
        write=csv.writer(archivo,delimiter=';')
        write.writerow(['DNI','Id del taller','Fecha de inscripcion','pago'])
        for i in range(self.__cantidad):
            self.__inscripciones[i].guardar(write)
        archivo.close()
