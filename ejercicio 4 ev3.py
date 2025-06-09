

todos_los_nombres=[]

while True:
    print("""*** MENÚ PRINCIPAL ***
1.- Ingresar nombre.
2.- Mostrar todos los nombres ingresados.
3.- Buscar un nombre.
4.- Salir del programa.
""")

    opcion=input("ingrese una opcion: ")
    try:
        opcion=int(opcion)
        if opcion <1 or opcion > 4:
            print("La opción debe ser 1, 2, 3 o 4.")
            continue
    except ValueError:
            print("Entrada invalida, ingrese un numero entero")
            continue
    if opcion==1:
        nombre_ingresado=input("ingrese un nombre: ")
        try:
            nombre_ingresado=str(nombre_ingresado)
            if not nombre_ingresado.isalpha():
                print("Nombre inválido. Intente nuevamente.")
                continue
            todos_los_nombres.append(nombre_ingresado)
            print("Nombre ingresado correctamente.")
        except ValueError:
            print("Nombre inválido. Intente nuevamente.")
            continue
    elif opcion==2:
        if todos_los_nombres:
            print("nombres ingresados: ")
            for nombre in todos_los_nombres:
                print("-", nombre)
        else:
            print("aun no se ingresan nombres :(")
    elif opcion==3:
        if todos_los_nombres:
            nombre_a_buscar=input("ingrese nombre: ")
            if nombre_a_buscar in todos_los_nombres:
                print(f"Nombre encontrado:'{nombre_a_buscar}'.")
            else:
                print(f"Nombre no encontrado'{nombre_a_buscar}' .")
        else:
            print("aun no hay nombres:(")
    elif opcion==4:
        print("Saliendo...")
        break



