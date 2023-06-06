from zope.interface import implementer
from Interfaz import Interfaz
from Nodo import Nodo
from Apoyo import Apoyo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
@implementer(Interfaz)
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def insertarElemento(self,elemento,pos):
        nodo=Nodo(elemento)
        error=False
        if pos==0:
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=self.__comienzo
            self.__tope+=1
        else:
            if self.__comienzo==None:
                error=True
            else:
                i=0
                ant=self.__comienzo
                aux=self.__comienzo
                while aux!=None and i!=pos:
                    ant=aux
                    aux=aux.getSiguiente()
                    i+=1
                if aux==None:
                    error=True
                else:
                    ant.setSiguiente(nodo)
                    nodo.setSiguiente(aux)
                    self.__tope+=1
        if error:
            raise IndexError
    def agregarElemento(self,elemento):
        nodo=Nodo(elemento)
        if self.__comienzo==None:
            self.__comienzo=nodo
            self.__actual=self.__comienzo
        else:
            aux=self.__comienzo
            ant=self.__comienzo
            while aux!=None:
                ant=aux
                aux=aux.getSiguiente()
            ant.setSiguiente(nodo)
            self.__tope+=1
    def mostrarElemento(self,pos):
        error=False
        if self.__comienzo==None:
            error=True
        else:
            i=0
            
            aux=self.__comienzo
            while aux!=None and i!=pos:
                
                aux=aux.getSiguiente()
                i+=1
            if aux==None:
                error=True
            else:
                tipo=''
                if type(aux.getDato())==Docente:
                    tipo='Docente'
                elif type(aux.getDato())==Apoyo:
                    tipo='Personal de Apoyo'
                elif type(aux.getDato())==Investigador:
                    tipo='Investigador'
                else:
                    tipo='Docente Investigador'
                print('El agente almacenado en la posicion:{},es:{}'.format(pos,tipo))
        if error:
            raise IndexError
    def ordenarPorNombre(self):
        cota=None
        k=None
        while(k!=self.__comienzo):
            k=self.__comienzo
            p=self.__comienzo
            while(p.getSiguiente()!=cota):
                if p.getDato().getNombre()>p.getSiguiente().getDato().getNombre():
                    aux=p.getSiguiente().getDato()
                    p.getSiguiente().setDato(p.getDato())
                    p.setDato(aux)
                    k=p
                p=p.getSiguiente()
            cota=k.getSiguiente()
   
    def mostrarDocentes(self,carrera):
        self.ordenarPorNombre()
        for dato in self:
            if isinstance(dato,DocenteInvestigador):
                if dato.getCarrera()==carrera:
                    print('{},{},carrera:{},cargo:{},area:{},tipo:{},categoria:{},importe:{}'.format(dato.getNombre(),dato.getCarrera(),dato.getCargo(),dato.getCatedra(),dato.getArea(),dato.getTipo(),dato.getCategoria(),dato.getImporteE()))
    def mostrarCantidad(self,area):
        cantidadUno=0
        cantidadDos=0
        for dato in self:
            if isinstance(dato,Investigador) or isinstance(dato,DocenteInvestigador):
                if dato.getArea()==area:
                    if type(dato)==Investigador:
                        cantidadUno+=1
                    elif type(dato)==DocenteInvestigador:
                        cantidadDos+=1
        print('Cantidad de investigadores:{}, cantidad de docentes de investigadores:{} en el area {}'.format(cantidadUno,cantidadDos,area))
    def listarAgentes(self):
        self.ordenarPorNombre()
        tipo=''
        for dato in self:
            if type(dato)==Apoyo:
                tipo='Apoyo'
            elif type(dato)==Investigador:
                tipo='Investigador'
            elif type(dato)==Docente:
                tipo='Docente'
            elif type(dato)==DocenteInvestigador:
                tipo='Docente Investigador'
            print('{}, {}, TIPO:{}, SUELDO:{}'.format(dato.getNombre(),dato.getApellido(),tipo,dato.calcularSueldo()))
    def mostrarPorCategoria(self,categoria):
        total=0.0
        for dato in self:
            if isinstance(dato,DocenteInvestigador):
                if dato.getCategoria()==categoria:
                    print('{},{},importe:{}'.format(dato.getApellido(),dato.getNombre(),dato.getImporteE()))
                    total+=dato.getImporteE()
        print('La cantidad total que la secretaria debe pedir al ministeripo es:{}'.format(total))
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__,personal=[personal.toJSON() for personal in self])
        return d
    def guardarArchivo(self,objectEncoder):
        diccionario=self.toJSON()
        objectEncoder.guardarJSONArchivo(diccionario,'personal.json')