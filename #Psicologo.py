#Psicologo


total_puntos=int(input("ingrese el total de puntos "))
if total_puntos == 0 and total_puntos<= 3:
    print("usted es un alumno de buen desempeño ")
    
elif total_puntos == 4 and total_puntos<=6:
    print("Usted es un alumno que puede mejorar  ")

elif total_puntos == 7 and total_puntos <=9:
    print("Usted es un alumno con algunos desafíos ")

elif total_puntos >= 10:
    print("Usted alumno con muchos desafíos ")
else:
    print("ingrese un digito valido")
