import json


def cargar(datos):
    datos = {}
    with open(datos, "r") as file:
        datos = json.load(file)
        return datos
    
def guardar(datos,archivo):
    datos = dict(datos)
    diccionario = json.dumps(datos, indent=4)

    file = open(archivo, "w")
    file.write(diccionario)
    file.close()