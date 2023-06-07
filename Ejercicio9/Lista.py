from zope.interface import implementer
from Nodo import Nodo
from Interface import Interfaz
from VehiculoNuevo import VehiculoNuevo
from VehiculoUsado import VehiculoUsado
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
            self.__tope+=1
        else:
            ant=self.__comienzo
            aux=self.__comienzo
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
            i = 0
            aux=self.__comienzo
            while aux!=None and i!=pos:
                aux=aux.getSiguiente()
                i+=1
            if aux==None:
                error=True
            else:
                if isinstance(aux.getDato(),VehiculoUsado):
                    print('El vehiculo de la posicion es usado')
                else:
                    print('El vehiculo es nuevo')
        if error:
            raise IndexError  
    def buscarPatente(self,patente,precio):
        i = 0
        bandera = False
        aux = self.__comienzo
        importe=0.0
        while aux!=None and not bandera:
            if isinstance(aux.getDato(),VehiculoUsado):
                if aux.getDato().getPatente()==patente:
                    aux.getDato().setPrecio(precio)
                    print('Precio base actual:{}'.format(aux.getDato().getPrecio()))
                    importe=aux.getDato().importeVenta()
                    print('Importe de venta es:{}'.format(importe))
                    bandera=True
                else:
                    aux=aux.getSiguiente()
        if not bandera:
            print('No se enocntro el vehiculo')
        
                       
    def mostrarEconomico(self):
        
        min=99999
        resultado=None
        aux=self.__comienzo
        while aux!=None:
            if aux.getDato().importeVenta()<min:
                min=aux.getDato().importeVenta()
                resultado=aux.getDato()
            aux=aux.getSiguiente()
            
        return resultado
    def buscarMin(self):
        
        economico=self.mostrarEconomico()
        if economico!=None:

            print('Modelo:{}'.format(economico.getModelo()))
            print('Cantidad de puertas{}'.format(economico.getCantidad()))
            print('Color:{}'.format(economico.getColor()))
            print('Precio Base:{}'.format(economico.getPrecio()))
            if isinstance(economico,VehiculoNuevo):
                print('**********Nuevo***********')
                print('Marca:{}'.format(economico.getMarca()))
                print('Version:{}'.format(economico.getVersion()))
                print('Importe de Venta:{}'.format(economico.importeVenta()))
            else: 
                if isinstance(economico,VehiculoUsado):
                    print('Marca:{}'.format(economico.getMarca()))
                    print('Patente:{}'.format(economico.getPatente()))
                    print('Año:{}'.format(economico.getAño()))
                    print('Kilometraje:{}'.format(economico.getKm()))
                    print('Importe de venta:{}'.format(economico.importeVenta()))
    def mostrarTodos(self):
        for dato in self:
            if dato!=None:
                print('Modelo:{}'.format(dato.getModelo()))
                print('Cantidad de puertas{}'.format(dato.getCantidad())) 
                if isinstance(dato,VehiculoNuevo):
                    print('Importe de venta{}'.format(dato.importeVenta()))
                else:
                    if isinstance(dato,VehiculoUsado):
                        print('Importe de venta{}'.format(dato.importeVenta()))
    def obtenerElemento(self,pos):
        vehiculo=None
        error=False
        if self.__comienzo==None:
            error=True
        else:
            i = 0
            aux=self.__comienzo
            while aux!=None and i!=pos:
                aux=aux.getSiguiente()
                i+=1
            if aux==None:
                error=True
            else:
                vehiculo=aux.getDato()
               
        if error:
            raise IndexError 
        return vehiculo  


     
  
        
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__, vehiculos=[vehiculo.toJSON()for vehiculo in self])

        return d
    def guardarArchivo(self,objectEncoder):
        diccionario=self.toJSON()
        objectEncoder.guardarJSONArchivo(diccionario,'vehiculos.json')
        