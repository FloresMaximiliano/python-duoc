# Validar registro de usuario
# Crea un programa que solicite nombre de usuario, correo y contraseña. Valida que:

# Todos los campos estén completos.

# El correo contenga un @.

# La contraseña tenga al menos 6 caracteres.

# Formulario de inscripción a un curso
# Pide al usuario nombre, edad y carrera.

# Verifica que la edad sea un número mayor a 17.

# No se aceptan campos vacíos.

# Encuesta de satisfacción (mínimo 1 respuesta)
# Pide 3 preguntas de opinión (pueden quedar vacías), pero al menos una debe tener respuesta. Si todas están vacías, mostrar un mensaje de error.

def validar(orden):
    campos_obligatorios=["usuario", "correo", "contraseña"]
    errores=[]
    
    for campo in campos_obligatorios:
        if campo not in orden or not orden[orden]:
            errores.append(f"el campo",{campo}, "es obligatorio")
    return errores
print("ingrese sus datos")
usuario=(input("nombre de usuario: ")).strip()
correo=(input("ingrese su correo: ")).strip()
contraseña=input("ingrese contraseña: ").strip()

if "@" in correo:
    correo=correo
else:
    print("el correo debe tener un @")

if len(contraseña) >=6:
    contraseña=contraseña
else:
    print("la contraseña debe tener minimo 6 cracteres.")


