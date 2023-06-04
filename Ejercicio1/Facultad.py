from Carrera import Carrera
 
class Facultad:
    __codigo=0
    __nombre=''
    __direccion=''
    __localidad=''
    __telefono=''
    __carreras=[]
    def __init__(self,codigo=0,nombre='',direccion='',localidad='',telefono='',lista=[]):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__carreras=[]
        for i in range (len(lista)):
            self.__carreras.append(Carrera(lista[i][0],lista[i][1],lista[i][2],lista[i][3],lista[i][4]))
    def getCodigo(self):
        return self.__codigo
    def __str__(self):
        return '{}'.format(self.__nombre)
    def verificarCarreras(self):
        for i in range(len(self.__carreras)):
            print(self.__carreras[i])
    def verificarNombre(self,nombre):
        i=0
        bandera=False
        indice=None
        while i<len(self.__carreras) and not bandera:
            if self.__carreras[i].getNombre()==nombre:
                bandera=True
                indice=i
            else:
                i+=1
        return indice
    def getNombre(self):
        return self.__nombre
    def getLocalidad(self):
        return self.__localidad
    def obtenerCodigo(self,nombre):
        pos=self.verificarNombre(nombre)
        if pos!=None:
            print('Codigo:{}'.format(self.__carreras[pos].getCodigo()+self.__carreras[pos].getCodigoCarrera()))
    def funcionTest(self):
        print('**********Funcion Test************')
        facultadUno=(Facultad('4','Facultad de Ciencias Sociales','Av.José Ignacio de la Roza Oeste 727','Rivadavia-San Juan','2644230414',[]))
        print('----------getCodigo----------')
        print('{}'.format(facultadUno.getCodigo()))
        print('--------str------------')
        print(facultadUno)
        print('---------verificar nombre de carreras----------')
        pos=self.verificarNombre('Ingeniería Electrónica')
        print('------------getLocalidad---------------')
        print('{}'.format(facultadUno.getLocalidad()))
        print('--------------getNombre----------------')
        print('{}'.format(facultadUno.getNombre()))