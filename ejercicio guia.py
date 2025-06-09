
carrito={}

while True:
    print("""
1.- Ingresar producto.
2.- Buscar producto.
3.- Eliminar producto.
4.- Salir.
""")
    opcion=input("Ingrese una opcion: ")
    try:
        opcion=int(opcion)
        if opcion<1 or opcion>4:
            print("ingrese una opcion valida")
    except ValueError:
        print("ingrese un numero entero.")
    
    if opcion==1:
        nombre=input("ingrese nombre del producto: ").lower()
        if nombre in carrito:
            print("ese producto ya existe!")
            continue
        else:
            try:
                cantidad=int(input(f"ingrese cantidad de '{nombre}': "))
                if cantidad<=0:
                    print("debe de ser mayor a 0")
                    continue
                precio=float(input(f"ingrese precio del producto '{nombre}': "))
            except ValueError:
                print("ingrese un valor valido para cantidad y precio")
                continue
            carrito[nombre]={"cantidad":cantidad,"precio":precio}
            print("producto agregado al carro!")
    elif opcion==2:
        buscar=input("ingrese el nombre del producto a buscar: ").lower()
        if buscar in carrito:
            producto=carrito[buscar]
            print(f"productoencontrado :{producto}")
            print(f"cantidad: {producto['cantidad']}")
            print(f"el precio es: {producto['precio']}")
        else:
            print(f"No se ha encontrado el producto... por lo que no se ha podido eliminar.")
    elif opcion==3:
        eliminar=input("ingrese nombre del producto que desee eliminar: ").lower()
        if eliminar in carrito:
            del carrito[eliminar]
            print(f"se ha eliminado el producto: {eliminar}")
        else:
            print("no se ha podido eliminar tal producto")
    elif opcion==4:
        print("saliendo...")
        break
