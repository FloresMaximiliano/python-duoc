## conversion de notas


nota=float(input("ingrese notas (del 1 hasta el 7): "))
if nota >= 1.0 and nota <= 3.9:
    print("insuficiente ")
elif nota >=4.0 and nota<= 4.9:
    print("aprobado")
elif nota >= 5.0 and nota<= 6.9:
    print("bueno")
elif nota==7.0:
    print("Excelente")
else:
    print("opcion invalida")
