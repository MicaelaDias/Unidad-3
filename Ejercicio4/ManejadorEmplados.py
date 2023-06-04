import csv
import numpy as np
from datetime import datetime

from Empleado import Empleado
from EmpleadoContratado import EmpleadoContratado
from EmpleadoDePlanta import EmpleadoDePlanta
from EmpleadoExterno import EmpleadoExterno

class ArregloEmpleados:
    __cantidad=0
    __dimension=0
    __incremento=5
    __empleados=None

    def __init__(self,dimension=0,incremento=5):
        self.__empleados=np.empty(dimension,dtype=Empleado)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=self.__incremento
    #dimension
    def redimensionarArreglo(self):
        self.__empleados.resize(self.__dimension)
    def verificarDimension(self):
        if self.__cantidad!=self.__dimension:
            self.__dimension=self.__cantidad
            self.redimensionarArreglo()
    def agregarElemento(self,empleado):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.redimensionarArreglo()
        self.__empleados[self.__cantidad]=empleado
        self.__cantidad+=1
    def cargarArchivo(self):
        archivo=open('contratados.csv',encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                EmpleadoContratado.setValor(float(fila[7]))
                self.agregarElemento(EmpleadoContratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],int(fila[6])))
        archivo.close()
        #externos
        archivo=open('externos.csv',encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                self.agregarElemento(EmpleadoExterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],float(fila[7]),float(fila[8]),float(fila[9])))
        archivo.close()
        #planta
        archivo=open('planta.csv',encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                self.agregarElemento(EmpleadoDePlanta(fila[0],fila[1],fila[2],fila[3],float(fila[4]),int(fila[5])))
        archivo.close()
    def buscarDni(self,dni):
        i = 0
        bandera=False
        indice=None
        while i <self.__cantidad and not bandera:
            if self.__empleados[i].verificarDni(dni):
                bandera=True
                indice=i
            else:
                i+=1
        return indice
    def incrementar(self,dni,cantidad):
        indice=self.buscarDni(dni)
        if indice!=None:
            if type(self.__empleados[indice])==EmpleadoContratado:
                self.__empleados[indice].acumularHoras(cantidad)
                print('Cantidad de horas{}'.format(self.__empleados[indice].getCantidad()))
    def mostrarMonto(self,tarea):
        total=0.0
        fechaActual=datetime.now()
        for i in range(self.__cantidad):
            if isinstance(self.__empleados[i],EmpleadoExterno):
                if self.__empleados[i].getTarea()==tarea:
                    if self.__empleados[i].getFecha()<str(fechaActual):
                        total+=self.__empleados[i].getCosto()
        print('total:{}'.format(total))

                        
    def listar(self):
        for i in range(self.__cantidad):
            if self.__empleados[i].sueldo()<150000:
                
                print('{},{},{}'.format(self.__empleados[i].getNombre(),self.__empleados[i].getDireccion(),self.__empleados[i].getDni()))
    def mostrarEmpleados(self):
        for i in range(self.__cantidad):
            print('Nombre:{},Sueldo:{},Telefono:{}'.format(self.__empleados[i].getNombre(),self.__empleados[i].sueldo(),self.__empleados[i].getTelefono()))