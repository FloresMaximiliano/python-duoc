# Desarrolle un programa en Python que permita ingresar dos números enteros que indiquen un rango numérico.
# El primer valor debe ser menor que el segundo. 
# Luego, en lugar de generar un número completamente aleatorio dentro de ese rango, el programa calculará
# el punto medio entre los dos números ingresados y, a partir de ahí, sumará o restará un valor aleatorio dentro del 20% del rango total.
import random

while True:
    try:
        mayor = int(input("Ingrese número superior: "))
        menor = int(input("Ingrese número menor: "))

        if mayor < 0 or menor < 0:
            print("Ambos números deben ser mayores o iguales a 0.")
            continue

        if mayor < menor:
            print("El número superior no puede ser menor que el número inferior.")
            continue

        break  
    except ValueError:
        print("Ingrese solo números enteros.")
punto_medio=(mayor-menor)/2
rango = mayor - menor
margen = 0.2 * rango
ajuste = random.uniform(-margen, margen)
numero_final = punto_medio + ajuste
print(f"el numero es: {numero_final}")