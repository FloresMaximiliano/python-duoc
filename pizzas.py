print("Bienvenido a Cesar's Pizza")
print("Menu:")
print("1.- PEPPERONI")
print("2.- QUESO")
print("3.- JAMÓN")
print("4.- 4N1")
print("5.- HULA HAWAIIAN")
print("6.- ULTIMATE SUPREME")
print("7.- VEGGIE")
print("8.- 3 MEAT TREAT")
print("9.- SUPER CHEESE 4N1")
print("10.- CHICKEN BBQ")
print("")

PEPPERONI= 5000
QUESO= 5500
JAMÓN = 6000
for_in_1= 7000
hula=7500
ultmate=8000
veggie=9000
three_meat=10000
super_cheese=12000
chiken_bbq= 13000

opcion = int(input("Elija su pizza. Ingrese el número de la pizza deseada: "))
cantidad = int(input("¿Cuantas pizzas desea?: "))
if opcion== 1:
    uno=PEPPERONI * cantidad
    print(uno)
elif opcion== 2:
    dos=QUESO* cantidad
    print(dos)
elif opcion==3:
    tres= JAMÓN * cantidad
    print(tres)
elif opcion==4:
    cuatro= for_in_1* cantidad
    print(cuatro)
elif opcion==5:
    cinco= hula*cantidad
    print(cinco)
elif opcion==6:
    seis=ultmate*cantidad
    print(seis)
elif opcion== 7:
    siete=veggie * cantidad
    print(siete)
elif opcion ==8:
    ocho=three_meat*cantidad
    print(ocho)
elif opcion == 9:
    nueve=super_cheese*cantidad
    print(nueve)
elif opcion == 10:
    diez= chiken_bbq*cantidad
    print(diez)
else:
        print("no teneos mas opciones de menu")


