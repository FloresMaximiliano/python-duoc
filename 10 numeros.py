
par=0
impar=0


print("ingrese 10 numeros")
for i in range(1,11):
    numeros_asumar=int(input())
    print("recolectando numeros...")
    if numeros_asumar%2==0:
        par=par+1
    else:
        impar=impar+1
print("par", par)
print("impar", impar)