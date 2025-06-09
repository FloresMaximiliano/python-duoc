# Formulario de inscripción a un curso
# Pide al usuario nombre, edad y carrera.

# Verifica que la edad sea un número mayor a 17.

# No se aceptan campos vacíos.


def validar(orden):
    campos_obligatorios = ["nombre", "edad", "carrera"]
    errores = []

    for campo in campos_obligatorios:
        if campo not in orden or not orden[campo]:
            errores.append(f"El campo '{campo}' le faltan datos.")
    return errores

print("Ingrese sus datos")
nombre = input("Ingrese su nombre: ").strip()
edad_input = input("Ingrese su edad: ").strip()

# Validamos que la edad sea numérica
if not edad_input.isdigit():
    print("La edad debe ser un número entero.")
else:
    edad = int(edad_input)
    carrera = input("Ingrese carrera: ").strip()

    datos = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }

    errores = validar(datos)

    if edad < 17:
        print("Debes ser mayor de 17 años.")
    elif errores:
        print("Errores en el formulario:")
        for error in errores:
            print("-", error)
    else:
        print("Su formulario ha sido registrado con éxito.")