def modificar(datos):
    datos = dict(datos)
    documento = documento = input("ingrese el numero postal de la ciuadad: ")
    numero = int(input("ingrese el numero de la venta: "))
    for i in range(len("venta")):
        if documento == datos["venta"][i]["documento"] and numero == datos["venta"][i]["numerov"]:
            datos["venta"][i]["nombre"] = nombre = input("ingrese el nuevo nombre: ")
            print("Catalogo de Productos")
            with open("filtro/filtro1/pagos.txt", "r") as file:
                lector = reader(file)
                for row in lector:
                    
                    print("__"*30)
                    print(row)
                    print("__"*30)
                    
            datos["venta"][i]["categoria"] = categoria = input("ingrese la nueva categoria: ")
            datos["venta"][i]["producto"] =  producto = input("ingrese el nuevo producto: ")
            datos["venta"][i]["nombrep"] = nombrep = input("ingrese el nuevo nombre : ")
            try:
                datos["venta"][i]["precio"]= precio = int(input("agrege el nuevo precio: "))
            except ValueError:
                print("numero invalido")
            try: 
                op1 = int(input("ingrese 1. para SI pago, 2. para NO pago: "))
                if op1 == 1:
                    datos["venta"][i]["pago"]= pago = "PAGO"
                    hora = datetime.datetime.now()
                    hora1 = hora.strftime("%y-%m-%d %H:%M:%S")
                    file = open("filtro/filtro1/pagos.txt", "w")
                    file.write("\n"+nombre +","+ documento +","+ categoria +","+ producto +","+ nombrep +","+ pago +","+ "FHECHA DE MODIFICACION"+ hora1 )
                    file.close

                elif op1 == 2:
                    datos["venta"][i]["pago"] = npago = "NO_PAGO"
                    hora = datetime.datetime.now()
                    hora1 = hora.strftime("%y-%m-%d %H:%M:%S")
                    file = open("filtro/filtro1/pagos.txt", "w")
                    file.write("\n"+nombre +","+ documento +","+ categoria +","+ producto +","+ nombrep +","+ npago +","+ "FHECHA DE MODIFICACION"+ hora1)
                    file.close
            except ValueError:
                print("numero invalido")
            return datos

        else: 
            print("=="*30)
            print("Modificacion Invalida")
            print("=="*30)
