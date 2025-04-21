## dar vuelta una cifra
invertir=0

num=int(input("ingrese un numero de tres cifras: "))
while num>0:
   num_invert= num%10
   invertir=invertir*10+num_invert
   num//= 10
print("Número invertido: ", invertir)
