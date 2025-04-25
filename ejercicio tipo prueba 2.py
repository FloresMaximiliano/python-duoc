opcion = ""



while opcion != "3":

  print("\n--- Teatro Moro ---")

  print("1. Comprar entrada")

  print("2. Ver tarifas")

  print("3. Salir")



  opcion = input("Seleccione una opción: ")



  if opcion == "1":

    print("\nTipos de entrada: 1.VIP, 2.Platea, 3.Tribuna, 4.Galería")

    entrada = input("Ingrese tipo de entrada: ")

    print("Tarifas disponibles: 1.Estudiante, 2.Publico general")

    tarifa = input("Ingrese tipo de tarifa: ")



    if entrada == "1":

      if tarifa == "1":

        total = 13000

      elif tarifa == "2":

        total = 25000

      else:

        print("Tarifa no válida.")

        continue



    elif entrada == "2":

      if tarifa == "1":

        total = 10000

      elif tarifa == "2":

        total = 19000

      else:

        print("Tarifa no válida.")

        continue



    elif entrada == "3":

      if tarifa == "1":

        total = 9000

      elif tarifa == "2":

        total = 11000

      else:

        print("Tarifa no válida.")

        continue



    elif entrada == "4" :

      if tarifa == "1":

        total = 6500

      elif tarifa == "2":

        total = 7200

      else:

        print("Tarifa no válida.")

        continue

    else:

      print("Tipo de entrada no válido.")

      continue



    print(f"\nTotal a pagar: ${total:,}")

    print("Gracias por su compra, disfrute la función.")



  elif opcion == "2":

    print("\n--- TARIFA POR TIPO DE ENTRADA ---")

    print("       Estudiante | Público general")

    print("VIP      $13.000   | $25.000")

    print("Platea    $10.000   | $19.000")

    print("Tribuna    $9.000   | $11.000")

    print("Galería    $6.500   | $7.200")



  elif opcion == "3":

    print("Saliendo del sistema...")



  else:

    print("Opción no válida. Intente nuevamente.")