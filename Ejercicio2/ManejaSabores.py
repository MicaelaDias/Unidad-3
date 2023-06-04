import csv
import numpy as np
from Sabor import Sabor
class ListaSabores:
    __cantidad=0
    __dimension=0
    __incremento=5
    __listaSabores=None

    def __init__(self, cantidad=0,dimension=0,incremento=5):
        self.__listaSabores=np.empty(dimension,dtype=Sabor)
        self.__cantidad=cantidad
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarSabor(self,sabor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaSabores.resize(self.__dimension)
        self.__listaSabores[self.__cantidad]=sabor
        self.__cantidad+=1
    def redimensionar(self):
        if self.__cantidad!=self.__dimension:
            self.__dimension=self.__cantidad
            self.__listaSabores.resize(self.__cantidad)
    def  cargarArchivo(self):
        archivo=open('sabores.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                self.agregarSabor(Sabor(fila[0],fila[1])) 
        archivo.close()
    def mostrarSabores(self):
        for i in range(self.__cantidad):
            print(self.__listaSabores[i])
    def buscarSabor(self,numero):
        i = 0
        bandera = False
        sabor = None
        while i<self.__cantidad and not bandera:
            if self.__listaSabores[i].getIdSabor()==numero:
                bandera = True
                sabor = self.__listaSabores[i]
            else:
                i+=1
        return sabor
    def ordenar(self):
        for i in range(self.__cantidad):
            min=i
            for j in range(self.__cantidad):
                if self.__listaSabores[i].getIdSabor()<self.__listaSabores[min].getIdSabor():
                    min=j
            aux=self.__listaSabores[i]
            self.__listaSabores[i]=self.__listaSabores[min]
            self.__listaSabores[min]=aux

    def saboresMasVendidos(self,cantidadMax):
        self.redimensionar()
        cantidad=0
        if self.__cantidad>5:
            cantidad=5
        else:
            cantidad=self.__cantidad
        for i in range(self.__cantidad):
            self.__listaSabores[i].setCantidad(cantidadMax)
            self.__listaSabores[::-1].sort()
        i=0
        bandera=True
        while i<self.__cantidad and bandera:
            if self.__listaSabores[i].getCantidad()==0:
                bandera=False
            else:
                print(self.__listaSabores[i])
                i+=1
        self.ordenar()
        