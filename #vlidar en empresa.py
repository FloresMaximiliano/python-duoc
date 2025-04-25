#vlidar en empresa
usuario= ""
numero_tel= 123
producto=""
cantidad=1123
pagar=""



print("ingese los siguientes datos para realizar su compra")
print("todos lo datos son obligarios")
usuario=(input("ingrese su nombre "))
if usuario == "":
        print("ingrese una nombre valido")
else:   
    numero_tel=int(input("ingrese un numero de telefono valido "))
    if numero_tel<=0 :
        print("ingrese numero valido")
    else:
        producto=input("ingrese producto ")
        cantidad=(int(input("ingrese cantidad ")))
        if producto == "" or cantidad <=0:
            print("ingrese numero valido")
        else:
            pagar=str(input("""¿esta seguro que desea pagar?
                                 ( 's'  o  'n' ) """))
            if pagar== "s":
                print( "nombre: ", usuario,
                       "Numero: ", numero_tel,
                       "Producto: ",producto,
                       "cantidad: ",cantidad
                          )
            elif pagar== "n":
                 print("compra cancelada")
            else:
                print("opcion invalida")
   