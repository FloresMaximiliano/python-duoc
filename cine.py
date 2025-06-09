# Construya un programa en Python que permita gestionar un sistema simple de venta de entradas para un cine
# por medio de un menú de opciones, el cual de un stock de entradas previamente cargadas (ejemplo 50 entradas),
# pueda realizar las distintas acciones.
# El programa debe mostrar un menú de opciones que permita al usuario:
# ***** Cine Estrella *****
# Bienvenido al sistema de venta de entradas del Cine Estrella
# 1.	Ver cuántas entradas quedan.
# 2.	Comprar una cantidad de entradas.
# 3.	Devolver  entradas.
# 4.	Salir del sistema.
# Si el usuario desea comprar entradas, se debe validar que haya suficiente cantidad disponible.
# En caso de que no haya suficientes, debe informarse al usuario.
# El programa debe repetirse hasta que el usuario elija la opción de salir.

total_entradas=[]
while True:
    print("""Bienvenido al sistema de venta de entradas del Cine Estrella
 1.	Ver cuántas entradas quedan.
 2.	Comprar una cantidad de entradas.
 3.	Devolver  entradas.
 4.	Salir del sistema.""")
    opcion=input("ingrese una opcion: ")
    try:
        opcion=int(opcion)
        if opcion<1 or opcion>4:
            print("debes de elejir una opcion (1,2,3 o 4).")
    except ValueError:
        print("ingresa solo numros enteros")
        continue
    if opcion==1:
        if total_entradas:
            print(f"el total de entradas es: {sum(total_entradas)}")
        else:
            print("aun no se ingresan Datos")
        continue
    elif opcion==2:
        comprar_entradas=input("ingrese La cantidad de entradas a comprar: ")
        try:
            comprar_entradas=int(comprar_entradas)
            if comprar_entradas < 0:
                print("ingrese un numero mayor a 0")
        except ValueError:
            print("ingrese solo numeros enteros")
        total_entradas.append(comprar_entradas)
        print(f"has ingresado exitosamente {comprar_entradas} entradas!")
        continue
    elif opcion==3:
        total=sum(total_entradas)
        devolver=input("ingrese cantidad a devolver: ")
        try:
            devolver=int(devolver)
            if devolver>total:
                print("no puedes devolver mas de lo que tienes")
        except ValueError:
            print("ingresa numeros enteros ")
        print(f"has devuleto{devolver} entradas.")
        total_entradas=total-devolver
        continue
    elif opcion==4:
        print("Saliendo...")
        break
