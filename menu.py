def menu_principal():
    print("=="*20)
    print("1. Registrar una Ciudad")
    print("2. Modifcar Informacion")
    print("3. Leer Informacion")
    print("4. Borrar la Informacion de una Ciudad")
    print("5. Salir")
    print("=="*20)
    
def modificar():
    print("=="*20)
    print("1. Modificar el Nombre de una Ciudad")
    print("2. Modificar el Codigo Postal de una Ciudad")
    print("3. Modificar Poblacion de una Ciudad")
    print("4. Modificar al Pais que pertence la Ciudad")
    print("5. Salir")
    print("=="*20)
    
def leer():
    print("=="*20)
    print("1. Leer Ciudades por Nombre")
    print("2. Leer Ciudades por Codigo Postal")
    print("3. Leer Ciudades por Pais")
    print("4. Leer por Ciudad")
    print("5. Leer por Pais")
    print("6. Leer por Codigo Postal")
    print("7. Leer por Mayor Poblacion")
    print("8. Leer por Menor Poblacion")
    print("9. Salir")
    print("=="*20)    

def opcion():
    try:
        op = int(input("ingrese la :"))
        return op
    except ValueError:
        print("numero invalido")