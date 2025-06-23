import random
import math
trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
    "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]
def asignar_sueldo():
    trabajadores_diccionario = [
        {
            "nombre": nombre,
            "sueldo": random.randint(300_000, 2_500_000)
        }
        for nombre in trabajadores
    ]
    return trabajadores_diccionario

sueldos_al_azar=asignar_sueldo()


def clasificar_sueldos():
    menores_a_800=[]
    for persona in sueldos_al_azar:
        if persona["sueldo"] <800_000:
            menores_a_800.append(persona)
    print(" Trabajadores Con sueldo menor a 800,000: ", len(menores_a_800))
    print(f"{"nombre del empleado":<20}{"sueldo":<10}")
    print("-" * 37)
    for persona in menores_a_800:
        print(f"{persona['nombre']:<25} ${persona['sueldo']:<9,}")
        print()

    entre_800_y_200=[]
    for persona1 in sueldos_al_azar:
        if persona1["sueldo"]>=800_000 and persona1["sueldo"]<= 2_000_000:
            entre_800_y_200.append(persona1)
    print("tabajadores con sueldo entre 800,000 y 2,000,000: ", len(entre_800_y_200))
    print(f"{"nombre del empleado":<20}{"sueldo":<10}")
    print("-"*37)
    for persona1 in entre_800_y_200:
        print(f"{persona1['nombre']:<25} ${persona1['sueldo']:<9,}")

    superior_a_200=[]
    for persona2 in sueldos_al_azar:
        if persona2["sueldo"]>2_000_000:
            superior_a_200.append(persona2)
    print("trabajadores con sueldo superior a 2,000,000: ",len(superior_a_200))
    print(f"{"nombre del trabajador":<20}{"sueldo":<10}")
    print("-"*37)
    for persona2 in superior_a_200:
        print(f"{persona2['nombre']:<25}{persona2['sueldo']:<9,}")

def Ver_estadisticas():
    trabajadores_info=asignar_sueldo()
    mas_produccion= max(trabajadores_info,key=lambda x: x["sueldo"])
    menos_produccion=min(trabajadores_info,key=lambda x: x["sueldo"])
    print(f"Maxima produccion {mas_produccion["nombre"]:<20}{mas_produccion["sueldo"]:,}")
    print(f"minima produccion: {menos_produccion["nombre"]:<20}{menos_produccion["sueldo"]:,}")
    sueldos=[trabajador["sueldo"] for trabajador in trabajadores_info]
    producto_total= math.prod(sueldos)
    media_geometrica= producto_total ** (1 / len(sueldos))
    print(f"la media geometrica es: {media_geometrica:,.0F}")


def reporte_sueldos():
    trabajadores_para_descuentos=asignar_sueldo()
    for trabajador in trabajadores_para_descuentos:
        sueldo_original=trabajador["sueldo"]
        descuento= sueldo_original*0.07
        sueldo_final_salud= sueldo_original - descuento
        print("salud")
        print()
        print(f"descuento de salud: {trabajador["nombre"]:<25} {sueldo_final_salud:,.0f}")
    for trabajador in trabajadores_para_descuentos:
        sueldo_original_para_afp=trabajador["sueldo"]
        descuento=sueldo_original*0.12
        sueldo_final_afp= sueldo_original_para_afp
        print("AFP")
        print()
        print(f"descuento de la afp: {trabajador["nombre"]} {sueldo_original_para_afp:,.0f}")
reporte_sueldos()