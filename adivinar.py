import random

x=0
numero_adivinar=random.randint(1,101)
print("""Adivine ingresando un numero""")
while x!= numero_adivinar:
    num_ingresado=int(input())
    if num_ingresado == numero_adivinar:
            print("Adivinaste!")
            break
    elif num_ingresado< numero_adivinar:
        print("muy bajo")
        
    elif num_ingresado > numero_adivinar:
        print("muy alto")
        
    


