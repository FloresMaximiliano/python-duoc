##calculadora
opcion= 0
while opcion != 5:
    opcion = int(input("""
 ==========Calculadora=========
 1. suma
 2. resta
 3.multiplicacion
 4. division
 5. salir
 """))
  ##SUMA:
    if opcion== int(1):
     print("suma")
     print("ingrese primer numero")
     num= int(input())
     print("ingrese segundo numero")
     num2=int(input())
     print("la suma es: ")
     print(num + num2)
  ##RESTA:
    elif opcion==int(2):
     print("Resta:")
     print("ingrese primer numero")
     num= int(input())
     print("ingrese segundo numero")
     num2=int(input())
     print("la Resta es: ")
     print(num-num2)
  #multiplicacion
    elif opcion==int(3):
     print("Multiplicacion:")
     print("ingrese primer numero")
     num= int(input())
     print("ingrese segundo numero")
     num2=int(input())
     print("la Multiplicacion es: ")
     print(num*num2)
  ##division
    elif opcion==int(4):
     print("Division:")
     print("ingrese primer numero")
     num= int(input())
     print("ingrese segundo numero")
     num2=int(input())
     if num2 == 0:
       print("Ingrese numeros Divibles distinto de 0 ")
     else:
      print("la Division es: ")
      print(num/num2)
if opcion== int(5):  
    print("Saliendo de la calculadora...")