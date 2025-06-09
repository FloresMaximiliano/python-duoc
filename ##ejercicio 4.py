##ejercicio 4
registro={}
while True:
    print("""
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
""")
    try:
        opcion=int(input("ingresa una opcion: "))
        if opcion<1 or opcion >4:
            print("ingresa una opciuon entre 1 y 4")
    except ValueError:
        print("debes ingresar un numero entero")
    if opcion==1:
        usuario=input("ingrese nombre de usuario: ").lower()
        if usuario in registro:
            print("este usuario ya existe!")
            continue
        sexo=input("ingrese sexo (M ,F): ").lower()
        if sexo in ("m","f"):
            print("se ha registrado el sexo!")
        else:
            print("ingrese una opcion valida (m, f)")
            continue
        contraseña=input("ingrese contraseña a registrar : ")
        errores= False
        if len(contraseña)<8:
            print("debe de ser al menos 8 caracteres")
            errores=True
        if not any(char.isdigit() for char in contraseña):
            print("tiene que tener al menos un numero")
            errores=True
        if not any(char.isalpha() for char in contraseña):
            print("debe de tener una letra")
            errores=True
        if ' ' in contraseña:
            print("no puede tener espacios")
            errores=True
        if errores:
            print("la contraseña no es valida.")
            continue
        else:
            print("contraseña ingresada correctamente!")
        print("usuario ingresado correctamente!")
        registro[usuario]={"sexo":sexo , "contraseña":contraseña}
    elif opcion==2:
        buscar=input("ingrese nombre de usuario a buscar: ").lower()
        if buscar in registro:
            resultado= registro[buscar]
            print(f"se ha encontrado a {buscar}")
            print(f"sexo: {resultado['sexo']}")
            print(f"la contraseña: {resultado['contraseña']}")
        else:
            print(f"no se ha encontrado a {buscar}")
    elif opcion==3:
        eliminar=input("ingrese el nombre de usuario a eliminar")
        if eliminar in registro:
            del registro[eliminar]
            print(f"se ha eliminado a {eliminar}")
        else:
            print(f"no se ha encontrado a {eliminar}")
    elif opcion==4:
        print("saliendo...")
        break


