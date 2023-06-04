import csv
import numpy as np
from TallerCapacitacion import TallerCapacitacion

class ArregloTaller:
    __cantidad=0
    __dimension=0
    __incremento=5
    __talleres=None

    def __init__(self,cantidad=0,dimension=0,incremento=5):
        self.__talleres=np.empty(dimension,dtype=TallerCapacitacion)
        self.__cantidad=cantidad
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarElemento(self,taller):
        if type(taller)==TallerCapacitacion:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.redimensionarArreglo()
            self.__talleres[self.__cantidad]=taller
            self.__cantidad+=1
        else:
            print('No se puede agregar.')
    def redimensionarArreglo(self):
        self.__talleres.resize(self.__dimension)
    def cargarArchivo(self):
        archivo=open('talleres.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                try:
                    self.__dimension=int(fila[0])
                except ValueError:
                    print('La primera fila  debe ser un entero')
                else:
                    self.redimensionarArreglo()
                bandera=not bandera
            else:
                self.agregarElemento(TallerCapacitacion(int(fila[0]),fila[1],int(fila[2]),int(fila[3])))
    def mostrar(self):
        for i in range(self.__cantidad):
            print('{},{},{}'.format(self.__talleres[i].getId(),self.__talleres[i].getNombre(),self.__talleres[i].getMonto()))
    def descontar(self,id):
        i = 0
        bandera=False
        while i<self.__cantidad and not bandera:
            if self.__talleres[i].getId()==id:
                self.__talleres[i].descontar(1)
                bandera=True
            else:
                i+=1
        return bandera
    def buscarTaller(self,id):
        i = 0
        bandera = False
        indice=None
        while i<self.__cantidad and not bandera:
            if self.__talleres[i].getId()==id:
                bandera=True
                indice=i
            else:
                i+=1
        return indice
    def buscarInscripcion(self,dni,id):
        resultado=False
        indice=self.buscarTaller(id)
        if indice!=None:
            pos=self.__talleres[indice].buscarInscripcion(dni)
            if pos!=None:
                resultado=True
        return resultado
    def inscribirPersona(self,pos,persona,fecha,pago,manejadorI,manejadorP):
        
        res=self.__talleres[pos].inscribirPersona(persona,fecha,pago)
        if res!=None:
            
            manejadorP.agregarElemento(persona)
           
            manejadorI.agregarElemento(res)
            manejadorP.mostrarDatos()
            manejadorI.mostrarInscripciones()
        
            descontar=self.descontar(self.__talleres[pos].getId())
            if descontar:
                print('se actualizo la cantidad de vacantes')
    def buscarPersona(self,dni,manejadorI):
        for i in range(self.__cantidad):
            res=self.__talleres[i].buscarInscripcion(dni)
            if res!=None:
                estado=manejadorI.verificarEstado(dni)
                if not estado:

                    print('taller:{} monto que adeuda:{}'.format(self.__talleres[i].getNombre(),self.__talleres[i].getMonto()))
    def mostrarInscriptos(self,id):
        indice=self.buscarTaller(id)
        
        if indice!=None:
            print('*****Listado de Inscriptos******')
            self.__talleres[indice].buscarInscriptos()