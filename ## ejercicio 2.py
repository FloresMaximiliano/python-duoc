## ejercicio 2
agenda={}

while True:
    print("""
    1.- Registrar cliente.
    2.- Consultar cliente.
    3.- Eliminar cliente.
    4.- Salir.
    """)
    opcion=int(input("ingrese una opcion: "))
    try:
        if opcion<1 or opcion>4:
            print("debe ingresar una opcion entre 1 y 4.")
    except ValueError:
        print("ingrese un numero entero.")
    if opcion==1:
        nombre=input("ingrese el nombre completo a registrar: ").lower()
        correo=input("ingrese correo electronico: ").lower()
        if "@" in correo:
            print("correo ingresado correctamente!")
        else:
            print("Debes ingresar un correo valido")
        edad=int(input("ingrese edad: "))
        try:
            if edad <18:
                print("Debes ser mayor de edad.")
        except ValueError:
            print("debe ingresar un numero entero")
        agenda[nombre]={"correo":correo,"edad":edad}
        print(f"se ha agregado {nombre} a tu agenda!")
    elif opcion==2:
        buscar=input("ingrese nombre a buscar en la agenda: ")
        if buscar in agenda:
            encontrado=agenda[buscar]
            print(f"se ha encontrado a {buscar} en tus contactos de agenda!" )
        else:
            print(f"no se ha podido encontrar a {buscar} en tus contactos")
    elif opcion==3:
        borrar=input("ingrese nombre del contacto que desea eliminar: ")
        if borrar in agenda:
            del agenda[borrar]
            print(f"se ha eliminado al contacto {borrar}")
        else:
            print("no se encuentra ese nombre en tu agenda...")
            continue
    elif opcion==4:
        print("Saliendo....")
        break
