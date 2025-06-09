


# Haga un menú que permita hacer las siguientes funcionalidades:

# *** MENU PRINCIPAL ***
# 1.- Ingresar número.
# 2.- Mostrar mayor.
# 3.- Mostrar promedio.
# 4.- Salir.

# La opción 1 debe permitir ingresar un número entero entre 0 y 100.
#  Si el usuario no ingresa un número entero, el programa debe entregar el mensaje: "Debe ingresar un número entero!!"
# , y repetir la solicitud de ingreso de número. Si se ingresa un número entero, pero no está dentro del rango [0,100] 
# entonces debe mostrar el mensaje: "Debe ingresar un número entre 0 y 100!!" 
# y repetir la solicitud de ingreso de número.
#  Si se ingresa un número que cumpla las condiciones, entonces debe mostrarse el mensaje: "Ingreso exitoso".

# La opción 2 debe mostrar el número mayor ingresado hasta ese momento.
# La opción 3 debe mostrar el promedio ingresado hasta ese momento.
# Para ambas opciones, si no se han ingresado números, y se pido el número mayor o promedio,
#  entonces el programa debe mostrar el mensaje: "No se han ingresado números."

# La opción 4 permite terminar el programa, mostrando por pantalla el mensaje: "Fin del programa. Adiós."
# En el menú principal, si se ingresa cualquier otro valor que no sea el de las opciones mostradas, 
# el programa debe mostrar el mensaje: "Debe ingresar una opción válida.”, y volver a preguntar por una opción.
total_numeros=[]
while True:
    print("""# *** MENU PRINCIPAL ***
# 1.- Ingresar número.
# 2.- Mostrar mayor.
# 3.- Mostrar promedio.
# 4.- Salir.""")
    opcion=input("ingrese una opcion: ")
    try:
        opcion=int(opcion)
        if opcion <1 and opcion > 4:
            print("debes seleccionar una opcion entre 1,2,3 y 4")
    except ValueError:
        print("Debes ingresar un numero entero")
    if opcion==1:
        num_ingresado=input("ingrese un numero: ")
        try:
            num_ingresado=int(num_ingresado)
            if num_ingresado<1 or num_ingresado>100:
                print("debe estar en un rango entre 1 y 100")
                continue
        except ValueError:
            print("ingrese un numero entreo")
        print("ingreso exitoso!")
        total_numeros.append(num_ingresado)
        continue
    elif opcion==2:
        if total_numeros:
            print(max(total_numeros))
            continue
        else:
            print("No hay numeros Ingresados")
    elif opcion==3:
        if total_numeros:
            promedio=sum(total_numeros)/len(total_numeros)
            print(promedio)
            continue
        else:
            print("no hay suficientes numeros para calcular el promedio")
            continue
    elif opcion==4:
        print("saliendo....")
        break
        

        