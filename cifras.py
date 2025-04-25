contador=0


numero=int(input("ingrese un numero "))

while numero>0:
    numero //=10
    contador += 1
print(f"El numero tiene {contador} cifras" )


