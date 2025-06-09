# •	Quintil de ingresos: Hay 5 quintiles en total (1 = menores ingresos, 5 = mayores ingresos).
# •	Condición laboral: Se considera si la persona está desempleada o empleada.

# Quintil	Condición Laboral	Subsidio de Arriendo
# 1 o 2	Desempleado	$350.000
# 1 o 2	Empleado	$280.000
# 3	Desempleado	$250.000
# 3	Empleado	$200.000
# Bonos Adicionales:
# •	Si el solicitante pertenece al Quintil 1 o 2, recibe un bono adicional de $60.000.
# •	Si además es mayor de 65 años, recibe $40.000 extra.
beneficio=0

quintil=int(input("ingrese quintil: "))
sit_economica=input("ingrese si esta desempleado o empleado: ")
edad=int(input("ingrese edad: "))

if (quintil==1 or quintil==2) and sit_economica == "desempleado":
    beneficio += 410_000
    if edad >65:
        beneficio+= 40_000
    print("su subsidio es de: ", beneficio)
elif (quintil==1 or quintil==2) and sit_economica == "empleado":
    beneficio+= 340_000
    if edad >65:
        beneficio+= 40_000
    print("Su subsidio es de :", beneficio)
elif (quintil==3) and sit_economica == "desempleado":
    beneficio+= 250_000
    if edad>65:
        beneficio+= 40_000
    print("su subsidio es de:", beneficio)
elif (quintil==3) and sit_economica== "empleado":
    beneficio+= 200_000
    if edad > 65:
        beneficio+= 40_000
    print("su subsidio es de: ",beneficio)
else:
    print("error")