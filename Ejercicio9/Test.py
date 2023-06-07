import unittest
from VehiculoUsado import VehiculoUsado
from VehiculoNuevo import VehiculoNuevo
from Lista import Lista


class TestVehiculo(unittest.TestCase):
    __lista=None

    def setUp(self):
        self.__lista=Lista()
        self.__vehiculoUno=VehiculoUsado('Palio',4,'gris',19200599,'Fiat','OER-400',2001,60000)
        self.__vehiculoDos=VehiculoUsado('Focus',4,'Blanco',13400500,'Ford','ADD-989',2000,58000)
        self.__vehiculoTres=VehiculoUsado('Palio',4,'ROJO',190000000,'Fiat','ABC-400',2000,100000)
        self.__vehiculoCuatro=VehiculoNuevo('Corolla cros',4,'Azul',23390800,'full')
    def testInsertarInicio(self):
        
        self.__lista.insertarElemento(self.__vehiculoUno,0)
        self.assertEqual(self.__lista.obtenerElemento(0),self.__vehiculoUno)
    
    def testInsertarFinal(self):
        self.__lista.insertarElemento(self.__vehiculoDos,0)
        self.assertEqual(self.__lista.obtenerElemento(0),self.__vehiculoDos)
    def testInsertarIntermedio(self):
        self.__lista.insertarElemento(self.__vehiculoCuatro,0)
        self.assertEqual(self.__lista.obtenerElemento(0),self.__vehiculoCuatro)
    def testAgregar(self):
        self.__lista.agregarElemento(self.__vehiculoTres)
        self.assertEqual(self.__lista.obtenerElemento(0),self.__vehiculoTres)
    def testObtener(self):
        self.assertEqual(self.__lista.obtenerElemento(0),self.__vehiculoUno)
    def testPrecio(self):
        self.__lista.buscarPatente('OER-400',20000000)
        self.assertEqual(self.__vehiculoUno.importeVenta(),1560000)