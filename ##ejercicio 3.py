##ejercicio 3

reservas={}
while True:
    print("""
    1.- Registrar cliente.
    2.- Consultar cliente.
    3.- Eliminar cliente.
    4.- Salir.
    """)
    try:
        opcion=int(input("ingrese una opcion: "))
        if opcion<1 or opcion>4:
            print("ingrersa una opcion entre 1 y 4")
            continue
    except ValueError:
        print("debe de ingresar un numero entero.")
    if opcion==1:
        huesped=input("ingrese nombre del huesped: ").lower()
        if huesped in reservas:
            print("este huesped ya esta tiene una reserva!")
            continue
        else:
            print(f"Se ha reguistrado exitosamente a {huesped}")
        try:
            noches=int(input("ingrese la cantidad de noches: "))
            if noches<0:
                print("debe de ser mayor que cero ")
                continue
        except ValueError:
            print("debes ingresar un numero entero")
        print(f"se han registrado {noches} noches!")
        habitacion=input("ingrese tipo de habitacion (individual,doble o suite): ").lower()
        if habitacion in ("individual" , "suite" , "doble"):
            print("se ha registrado exitosamente")
        else:
            print("ingrese una opcion valida")
            continue
        reservas[huesped]={ "noches": noches,"habitacion": habitacion}
    elif opcion==2:
        buscar=input("ingrese nombre del huesped: ").lower()
        if buscar in reservas:
            encontrado=reservas[buscar]
            print(f"se ha encontrado a {buscar} ")
            print(f"su habitacion: {encontrado['habitacion']}")
            print(f"sus noches: {encontrado['noches']}")
        else:
            print("no hay reservas para con ese nombre")
    elif opcion==3:
        cancelar=input("ingrese nombre del titular de la reserva para dar de baja: ").lower()
        if cancelar in reservas:
            del reservas[cancelar]
            print(f"se ha eliminado la reserva de {cancelar}")
        else:
            print("no hay reservas con ese nombre")
    elif opcion==4:
        print("saliendo....")
        break


        


