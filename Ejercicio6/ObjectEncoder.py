import json
from pathlib import Path
from Lista import Lista
class ObjectEncoder:
    def decodificarDiccionario(self,d):
        resultado=None
        if '__class__' not in d: 
            resultado = d 
        else: 
            class_name=d['__class__'] 
            class_=eval(class_name) 
            if class_name=='Lista': 
                vehiculos=d['vehiculos'] 
                dVehiculos = vehiculos[0] 
                lista=class_() 
                for i in range(len(vehiculos)): 
                    dVehiculos=vehiculos[i]
                    class_name=dVehiculos.pop('__class__')
                    class_=eval(class_name) 
                    atributos=dVehiculos['__atributos__'] 
                    unVehiculo=class_(**atributos) 
                    lista.agregarElemento(unVehiculo) 
            resultado=lista
        return resultado   
    def guardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open('w',encoding='UTF-8') as destino:
            json.dump(diccionario, destino, indent=4) 
            destino.close() 
    def leerJSONArchivo(self,archivo):
        resultado=-1
        try:
            with Path(archivo).open(encoding='UTF-8') as fuente:
                diccionario=json.load(fuente)
                fuente.closed()
        except FileNotFoundError:
            print('El archivo vehiculos.json no existe,no se cargaron datos')
        else:
            resultado=diccionario
        return resultado
    def convertirTextoADiccionario(self,texto):
        return json.loads(texto)