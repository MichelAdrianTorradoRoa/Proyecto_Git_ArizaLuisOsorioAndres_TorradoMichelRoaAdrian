from menu import *
from cargardatos import *
from borrar import *
from registrar import *
from leer import *
ruta = "/datos.json"

datos = cargar(ruta)

while True:
    menu_principal()
    op = opcion()
    if op == 1:
        datos = registrar(datos)
    elif op == 2:
        datos = modificar(datos)
    elif op == 3:
        datos= consultar(datos)
    elif op == 4:
        datos= borrar(datos)
    elif op == 5:
        print("Adios!")
        break
    

guardar(datos,ruta)