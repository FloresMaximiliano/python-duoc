




while True:
    num_ingresado=(input("ingrese cantidad de frases a evaluar: "))
    try:
        numero=int(num_ingresado)
        if numero >0:
            break
        else:
            print("debe ser un numero mayor que cero. ")
    except ValueError:
        print("Entrada invalida, ingrese un numero entero")
es_palindromo=0
no_palindromo=0
def palindromo(frase):
    frase = frase.lower().replace(" ", "").replace(",", "").replace(".", "")
    return frase==frase [::-1]

for i in range(numero):
    while True:
        frase_ingresada = str(input("ingrese frase: "))
        if frase_ingresada.strip():
            if palindromo(frase_ingresada):
                print("Es un palíndromo")
                es_palindromo+=1
            else:
                print("No es un palíndromo")
                no_palindromo+=1
            break
        else:
            print("La frase no puede estar vacía.")
print(f"se ingresaron {es_palindromo} palindromos")
print(f"se ingresaron {no_palindromo} frases que no son palindromos")