




while True:
    num_ingresado=(input("ingrese cantidad de numeros a evaluar: "))
    try:
        numero=int(num_ingresado)
        if numero >0:
            break
        else:
            print("debe ser un numero mayor que cero. ")
    except ValueError:
        print("Entrada invalida, ingrese un numero entero")
primo=0
no_primo=0
for i in range(1,numero+1):
    while True:
        num_evaluar=input(f"Ingrese numero {i}: ")
        try:
            num_evaluar=int(num_evaluar)
            if num_evaluar >0:
                break
            else:
                print("debe ser un numero mayor que cero. ")
        except ValueError:
            print("la entrada tiene que ser un numero entero :(")
    if num_evaluar == 1:
        print("1 no es primo")
        no_primo+=1
    else:
        for x in range(2, num_evaluar):
            if num_evaluar % x == 0:
                print(f"{num_evaluar} no es primo")
                no_primo+=1
                break
        else:
            print(f"{num_evaluar} es primo")
            primo+=1
print(f"los numeros primos en total fueron {primo} ")
print(f"los numeros no primos fueron {no_primo}")