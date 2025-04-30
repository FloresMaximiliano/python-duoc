# Formulario de inscripción a un curso
# Pide al usuario nombre, edad y carrera.

# Verifica que la edad sea un número mayor a 17.

# No se aceptan campos vacíos.


def validar(orden):
    campos_obligatorios=["nombre","edad","carrera"]
    errores=[]

    for campo in campos_obligatorios:
        if campo not in orden or not orden[campo]:
            errores.append(f"el campo",{campo},"le faltan datos")
    return errores
print("ingrese sus datos")
nombre=input("ingrese su nombre: ").strip()
edad=int(input("ingrese su edad: ").strip())
carrera=input("ingrese carrera: ").strip()
if edad<17:
    print("debes ser mayor de 17 años")
elif edad>17 and campos_obligatorios = True:
    print("su formulario ha sido reguistrado con exito")
else:
    print("ingrese correctmente los datos")