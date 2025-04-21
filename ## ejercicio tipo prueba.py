## ejercicio tipo prueba
# CANTIDAD DE ASISTENTES	TARIFAS
# 	      PRECIO UN MENÚ	PRECIO DOS OPCIONES DE MENÚ
# Hasta 50	$1.000.000	         $1.500.000
# Hasta 100	$1.800.000	         $2.300.000
# Hasta 200	$3.500.000	         $4.000.000
# Hasta 300	$4.100.000	         $4.600.000



# Eventos “Food and Dance”
# Hasta 50 personas                $1.000.000 Una opción de menú
# Buffet de Postres		$ 500.000
# Total  				$1.500.000

# si quiere dos opciones de menú y si desea agregar buffet de postres.

## Menu
print("""
      ==Bienvenido a Food & Dance==
     CANTIDAD DE ASISTENTES	       TARIFAS
 	 PRECIO UN MENÚ	            PRECIO (con bufet)
 Hasta 50	$1.000.000	         $1.500.000
 Hasta 100	$1.800.000	         $2.300.000
 Hasta 200	$3.500.000	         $4.000.000
 Hasta 300	$4.100.000	         $4.600.000""")

## Listas
def cotizar(asistentes):
    tarifa = [
    (50,     1000000, 1500000),          ## tupla
    (100,    1800000, 2400000),  
    (200,    3500000, 4000000),
    (300,    4100000, 4600000),
]
    ##funcion 
    for limite, precio_un_menu,precio_buffet in tarifa:          ## Recorre la tupla 
        if asistentes<=limite:                            ##condicional
            return precio_un_menu, precio_buffet

    return None,None 

## Solicitud
asistentes=int(input(("ingrese cantidad de asistentes: ")))
menu,buffet = cotizar(asistentes)

if menu is not None:                                            #verificacion
    print(f"Para {asistentes} asistentes:")
    print(f"-precio con un menu: ${menu:,}")
    print(f"-precio con buffet: ${buffet:,}")
else:
    print("no ofrecemos servicio para mas de 300 personas")