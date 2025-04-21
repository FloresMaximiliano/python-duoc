
Contraseña_ingresada=0
contraseña = 12
while True:
    Contraseña_ingresada=int(input("ingrese contraseña: "))
    if Contraseña_ingresada==contraseña:
        print("Bienvenido")
        break
    elif Contraseña_ingresada!=contraseña:
        print("Contraseña invalida")


