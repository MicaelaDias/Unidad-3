import csv
from Facultad import Facultad
from Carrera import Carrera
class ManejadorFacultades:
    __listaFacultad=[]

    def __init__(self):
        self.__listaFacultad=[]
    def agregarFacultad(self,facultad):
        if type(facultad)==Facultad:
            self.__listaFacultad.append(facultad)
        else:
            print('No se puede agregar la facultad')
    def cargarArchivo(self):
        archivo=open('Facultades.csv',encoding='utf8')
        reader=csv.reader(archivo,delimiter=',')
        listaCarreras=[]
        listaFacultad=None
        bandera=True
        for fila in reader:
            if bandera:
                listaFacultad=fila
                
                bandera=False
            else:
                if listaFacultad[0]==fila[0]:
                    listaCarreras.append(fila)
                else:
                    self.agregarFacultad(Facultad(int(listaFacultad[0]),listaFacultad[1],listaFacultad[2],listaFacultad[3],listaFacultad[4],listaCarreras))
                    listaFacultad=fila
                    
                    listaCarreras=[]
        
        self.agregarFacultad(Facultad(int(listaFacultad[0]),listaFacultad[1],listaFacultad[2],listaFacultad[3],listaFacultad[4],listaCarreras))
        archivo.close()
    def buscarCodigo(self,codigo):
        i = 0
        indice = None
        bandera = False
        while i<len(self.__listaFacultad) and not bandera:
            if self.__listaFacultad[i].getCodigo()==codigo:
                bandera=True
                indice=i
            else:
                i+=1
        return indice
    def buscarFacultad(self,codigo):
        indice=self.buscarCodigo(codigo)
        if indice!=None:
            print(self.__listaFacultad[indice])
            self.__listaFacultad[indice].verificarCarreras()
    def buscarNombre(self,nombre):
        i=0
        bandera=False
        indice=None
        
        while i<len(self.__listaFacultad) and not bandera:
            pos=self.__listaFacultad[i].verificarNombre(nombre)
            if pos!=None:
                bandera=True
                indice=i
            else:
                i+=1
        return indice
    def buscarCarrera(self,nombre):
        indice=self.buscarNombre(nombre)
        if indice!=None:
            self.__listaFacultad[indice].obtenerCodigo(nombre)
            print('Facultad:{}, Localidad:{}'.format(self.__listaFacultad[indice].getNombre(),self.__listaFacultad[indice].getLocalidad()))
    def funcionTest(self):
        print('------Agregar Facultad-------')
        facultad=(Facultad(3,'Facultad de Filosofia Humanidades y Artes','Av.José Ignacio de la Roza Oeste 230 J5400 San Juan','Capital-San Juan','02644222643',[]))
        self.agregarFacultad(facultad)
        print('----Buscar Codigo de Facultad-------')
        pos=self.buscarCodigo(3)
        print('------Buscar Facultad-----------')
        self.buscarFacultad(3)
        print('------Buscar Carrera---------')
        self.buscarCarrera('BioIngenieria')           