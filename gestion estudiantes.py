opcion=0
registrado= False
while opcion != 4:
    opcion = int(input("""Menú de Gestión de Estudiantes
1. Registrar estudiante
2. Listar estudiante registrado
3. Buscar estudiante
4. Salir
                    """))
    if opcion==1:
        print("ingrese nombre")
        nombre_estudiante=input()
        print("ingrese edad")
        edad_estudiante=  input()
        print("ingrese promedio")
        promedio_estudiante= input()
        print("estudiante registrado con exito")
        registrado=True
    elif opcion==2:
        if registrado:
            print("Estudiante registrado:")
            print("Nombre:", nombre_estudiante)
            print("Edad:" , edad_estudiante)
            print("Promedio:", promedio_estudiante)
        else:
            print("estudiante no registrado")
    elif opcion==3:
        print("ingrese nombre a buscar")
        buscar=input()
        if registrado and buscar == nombre_estudiante:
            print("estudiante Encontrado")
            print("Nombre:", nombre_estudiante)
            print("edad", edad_estudiante)
            print("promedio:", promedio_estudiante)
        else:
            print("estudiante no encontrado")
    elif opcion==4:
        print("saliendo...")
    else:
        print("opcion no valida.")
            