# Combos





print("""1. combo letal burger doble
         2. combo letal burger simple
         3. duo box
         4. promo para 3
         5.promo duo
         6.big promo
         7. party box""")
cuantos_combos=input("cantidad de combos: ")
num_primer_combo=int(input("ingrese en numero del primer combo o priomo: "))
num_segundo_combo=int(input("ingrese el numero combo o promo: "))
if num_primer_combo==3:
    bebida1=input("que bebida?: fanta (f), sprite (s), limon soda(l):  ")
    if bebida1== "f" or "s" or "l":
        bebida1=bebida1
    hamburguesa1=input("¿que hamburguesa?: especial (e), vegetariana(v), extra(x): ")
    if hamburguesa1== "e" or "v" or "x":
        hamburguesa1=hamburguesa1
    acompañamiento1=input("¿que acompañamiento?: papas (p), empanadas (e), nugget(n): ")
    if acompañamiento1== "p" or "e" or "n":
        acompañamiento1==acompañamiento1
    print("personalizacion de combo2")
    combo3=(bebida1,
            hamburguesa1,
            acompañamiento1)

    if num_segundo_combo==7:
        bebida2=input("que bebida?: fanta (f), sprite (s), limon soda(l):  ")
        if bebida2== "f" or "s" or "l":
            bebida2==bebida2
        hamburguesa2=input("¿que hamburguesa?: especial (e), vegetariana(v), extra(x): ")
        if hamburguesa2== "e" or "v" or "x":
            hamburguesa2=hamburguesa2
        acompañamiento2=input("¿que acompañamiento?: papas (p), empanadas (e), nugget(n): ")
        if acompañamiento2== "p" or "e" or "n":
            acompañamiento2==acompañamiento2
            combo7=(bebida2,
            hamburguesa2,
            acompañamiento2)

for i in range (1, cuantos_combos +1):
    print("combo", combo3 if i == 1 else combo7)
    if i ==1:
        if bebida1 == "f":
            print("babida: fanta")
        elif bebida1 == "s":
            print("bebida: sprite")
        elif bebida1 == "l":
            print("bebida:limon soda")
        if hamburguesa1 == "e":
            print("hamburgesa:especial")
        elif hamburguesa1 == "v":
            print("hamburguesa: vegetariana")
        elif hamburguesa1 == "x":
            print("hamburguesa: extra")
        if acompañamiento1 == "p":
            print("acompañamiento: papas")
        elif acompañamiento1 == "e":
            print("acompañamiento: empanada")
        elif acompañamiento1 == "n":
            print("acompañamiento: nuggets")
        