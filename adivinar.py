import random



numero_adivinar=random.randint(1,101)
print("""Adivine ingresando un numero""")
num_ingresado=int(input())
if num_ingresado == numero_adivinar:
    print("Adivinaste!")
elif num_ingresado< numero_adivinar:
    print("muy bajo")
elif num_ingresado > numero_adivinar:
    print("muy alto")
    


