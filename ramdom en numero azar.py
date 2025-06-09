

import random
errores=0
primer_limite=int(input("ingrese primer parametro: " ))
segundo_limite=int(input("ingrese segundo limite: "))

x=random.randint(primer_limite,segundo_limite)
while errores<3:

    num_ingresado=int(input("ingrese un numero para adivinar: "))
   
    if num_ingresado==x:
        print("ganaste! ")
        break
    elif num_ingresado < x:
        print("el numero es mayor! ")
        errores+=1
    elif num_ingresado > x:
        print("el numero es menor! ")
        errores+=1
    if errores==3:
            print("has llegado al limite de intentos:( ")
