

total_numeros_ingresados=[]
while True:
    print("""*** MENU PRINCIPAL ***
1.- Ingresar número.
2.- Mostrar mayor.
3.- Mostrar menor.
4.- Salir.
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
        while True:
            num_ingresado=input("ingrese un numero: ")
            try:
                num_ingresado=int(num_ingresado)
                if num_ingresado >0 and num_ingresado < 100:
                    print("ingreso exitoso")
                    total_numeros_ingresados.append(num_ingresado)
                    break
                else:
                    print("Debe ser un numero entre 0 y 100")
            except ValueError:
                print("Entrada invalida, ingrese un numero entero")

    elif opcion==2:
        if total_numeros_ingresados:
            print(max(total_numeros_ingresados))
        else:
            print("no se han ingresado numeros aun :(")

    elif opcion==3:
        if total_numeros_ingresados:
            print(min(total_numeros_ingresados))
        else:
            print("no se han ingresado numeros aun :(")
    elif opcion==4:
        print("Saliendo...")
        break

