from ObjectEncoder import ObjectEncoder
from Menu import Menu
from Lista import Lista
if __name__=='__main__':
    objectEncoder=ObjectEncoder()
    lista=None
    archivo='vehculos.json'
    diccionario=objectEncoder.leerJSONArchivo('vehiculos.json')
    if diccionario!=-1:
        lista=objectEncoder.decodificarDiccionario(diccionario)
        print('Se cargaron los datos en el archivo')
    else:
        lista=Lista()
    menu=Menu()
    menu.lanzarMenu(lista,objectEncoder)