
def registrar (datos):
    datos = dict(datos)
    consulta = {}       
    consulta["nombre"] = nombre = input("ingrese el nombre de la ciudad: ")
    while True:
        op = int(input("1 para agregar ciudad, 2. salir: "))
        if op == 1:
            consulta["pais"]= pais = input("agregue pais: ")
            try:
                consulta["codigo postal"] = codigo = int(input("agregue codigo postal: "))
                consulta["poblacion"] = int(input("agregue la poblacion de la ciudad: "))
            except ValueError:
                print("numero invalido")
        elif op == 2:
            
            break
        else:
            print("opcion invalida")
    print("=="*30)
    print("ciudad registrada")
    print("=="*30)
    datos[""].append()
    return datos