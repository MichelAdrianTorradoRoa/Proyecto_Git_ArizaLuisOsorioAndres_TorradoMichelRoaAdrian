

def borrar(datos):
    datos = dict(datos)
    ciudad = ciudad = input("ingrese la ciudad que desea eliminar: ")
    for i in range(len("consulta")):
        if ciudad == datos["consulta"][i]["ciudad"]:
            datos["consulta"].pop(i)
            print("Ciudad eliminada")
        return datos