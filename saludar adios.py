opcion=0
while opcion!=3:
    opcion= int(input("""===========menu======= 
    1.saludar 
    2.despedirce 
    3.salir
                      """))
    if opcion==1:
        print("hola")
    elif opcion==2:
        print("adios")
    else:
        print("saliendo...")
