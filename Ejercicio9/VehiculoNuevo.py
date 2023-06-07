from Vehiculo import Vehiculo
class VehiculoNuevo(Vehiculo):
    __marca='Toyota'
    __version=''

    @classmethod
    def getMarca(cls):
        return cls.__marca
    def __init__(self, modelo='', cantidad=0, color='', precio=0,version=''):
        super().__init__(modelo, cantidad, color, precio)
        self.__version=version
    def getVersion(self):
        return self.__version
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            atributos=dict(
            super().toJSON(),marca=self.getMarca(),version=self.__version)
            )
        return d
    def importeVenta(self):
        porcentaje=self.getPrecio()*0.10
        importe=self.getPrecio()+porcentaje
        if self.__version=='full':
            importe+=self.getPrecio()*0.02

        return importe
