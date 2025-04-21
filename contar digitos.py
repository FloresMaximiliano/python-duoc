num_ingresado=int(input("ingrese un numero: "))
digito=[]
while num_ingresado>0:
    digito.insert(0,num_ingresado%10)
    num_ingresado//=10
for i in digito:
    print(i)

