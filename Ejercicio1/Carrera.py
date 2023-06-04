class Carrera:
    __codigoF=0
    __codigo=0
    __nombre=''
    __titulo=''
    __duracion=''
    __grado=''

    def __init__(self,codigoF=0,codigo=0,nombre='',titulo='',duracion='',grado=''):
        self.__codigoF=codigoF
        self.__codigo=codigo
        self.__nombre=nombre
        self.__titulo=titulo 
        self.__duracion=duracion
        self.__grado=grado
    def getCodigo(self):
        return self.__codigoF
    def __str__(self):
        return '{},{}'.format(self.__nombre,self.__duracion)
    def getNombre(self):
        return self.__nombre
    def getCodigoCarrera(self):
        return self.__codigo
    def funcionTest(self):
        print('********Funcion Test Carrera*********')
        carreraUno=Carrera('2','4','Biologia','Biologo','Once semtestres','Grado')
        print('--------getCodigo--------')
        print('{}'.format(carreraUno.getCodigo()))
        print('---------getNombre-----------')
        print('{}'.format(carreraUno.getNombre()))
        print('------getCodigoCarrera--------')
        print('{}'.format(carreraUno.getNombre()))
