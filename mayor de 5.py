mayor=0


print("ingrese cinco numeros")
for i in range(1,6):
    fivenum=int(input())
    if fivenum > mayor:
        mayor= fivenum
print("numero mayor es", mayor)
