def validar_orden(orden):
    campos_obligatorios = ['nombre', 'email', 'direccion', 'telefono', 'carrito']
    errores = []

    for campo in campos_obligatorios:
        if campo not in orden or not orden[campo]:
            errores.append(f"El campo '{campo}' es obligatorio y no ha sido proporcionado.")

    return errores

# Solicitar datos al usuario
print("Ingrese los datos de su orden de compra:")

nombre = input("Nombre completo: ").strip()
email = input("Correo electrónico: ").strip()
direccion = input("Dirección de envío: ").strip()
telefono = input("Número de teléfono: ").strip()

# Simulamos que el cliente agrega productos
carrito = []
while True:
    producto = input("Ingrese un producto al carrito (o escriba 'fin' para terminar): ").strip()
    if producto.lower() == 'fin':
        break
    if producto:
        carrito.append(producto)

# Crear el diccionario con los datos ingresados
orden_cliente = {
    'nombre': nombre,
    'email': email,
    'direccion': direccion,
    'telefono': telefono,
    'carrito': carrito
}

# Validar la orden antes de procesar el pago
errores_encontrados = validar_orden(orden_cliente)

if errores_encontrados:
    print("\n❌ No se puede procesar el pago debido a los siguientes errores:")
    for error in errores_encontrados:
        print("-", error)
else:
    print("\n✅ Todos los datos están completos. Procediendo con el pago...")