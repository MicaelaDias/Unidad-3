from Vehiculo import Vehiculo
class VehiculoUsado(Vehiculo):
    __marca=''
    __patente=''
    __año=0
    __kilometraje=0

    def __init__(self, modelo='', cantidad=0, color='', precio=0,marca='',patente='',año=0,km=0):
        super().__init__(modelo, cantidad, color, precio)
        self.__marca=marca
        self.__patente=patente
        self.__año=año
        self.__kilometraje=km
    def getPatente(self):
        return self.__patente
    def getMarca(self):
        return self.__marca
    def getAño(self):
        return self.__año
    def getKm(self):
        return self.__kilometraje
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
            super().toJSON(),marca=self.__marca,patente=self.__patente,año=self.__año,km=self.__kilometraje
            )
        )
        return d
    def importeVenta(self):
        importe=0.0
       
        antiguedad=2023-self.__año
        porcentaje=self.getPrecio()*0.01
        importe=self.getPrecio()-porcentaje*antiguedad
        if self.__kilometraje>100000:
            importe-=self.getPrecio()*0.02
        return importe