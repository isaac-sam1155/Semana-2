print("Bienvenido al museo de antropología e historia :D")
print("------------------------------------------------")
print("vamos a generar tu ticket")
print("------------------------------------------------")
print("ofrecemos distintos precios y descuentos")
print("son los siguientes:")
print("------------------------------------------------")
print("precios: ")
print("menos de 3 años: gratis")
print("de 3 a 17 años: $30")
print("18 o más: $45")
print("------------------------------------------------")
print("descuentos: ")
print("adulto mayor (60 años o más): 12% de descuento")
print("tipo 1: estudiante, 10% de descuento")
print("tipo 2: maestro, 10% de descuento")
print("tipo 3: ninguno, sin descuento")
print("------------------------------------------------")


PRECIO_NINO = 0
PRECIO_MENOR = 30
PRECIO_ADULTO = 45

DESCUENTO_ADULTO_MAYOR = 0.12
DESCUENTO_ESTUDIANTE = 0.10
DESCUENTO_MAESTRO = 0.10
DESCUENTO_NINGUNO = 0


visitantes = 0
total_descuentos = 0
total_pagar = 0


while True:


    entrada = input("Escribe la edad del visitante (o 'fin' para cerrar): ")

    if entrada.lower() == "fin":
        break

    try:
        edad = int(entrada)

        if edad < 0 or edad > 110:
            print("Edad no válida, escribe una edad entre 0 y 110")
            continue

    except ValueError:
        print("Error, escribe la edad con números, no con letras")
        continue


    if edad < 3:
        precio_base = PRECIO_NINO
    elif edad <= 17:
        precio_base = PRECIO_MENOR
    else:
        precio_base = PRECIO_ADULTO


    descuento_porcentaje = 0
    tipo_nombre = "Ninguno"


    if edad >= 18:


        while True:
            try:
                tipo = int(input(
                    "Tipo: 1) Estudiante  2) Profesor  3) Ninguno: "
                ))

                if tipo >= 1 and tipo <= 3:
                    break
                else:
                    print("Opción no válida, escribe un número del 1 al 3")

            except ValueError:
                print("Error, escribe el tipo de visitante con números, no con letras")


        if edad >= 60:
            descuento_porcentaje = DESCUENTO_ADULTO_MAYOR
            tipo_nombre = "Adulto mayor"
        elif tipo == 1:
            descuento_porcentaje = DESCUENTO_ESTUDIANTE
            tipo_nombre = "Estudiante"
        elif tipo == 2:
            descuento_porcentaje = DESCUENTO_MAESTRO
            tipo_nombre = "Profesor"
        else:
            descuento_porcentaje = DESCUENTO_NINGUNO
            tipo_nombre = "Ninguno"


    descuento = precio_base * descuento_porcentaje
    paga = precio_base - descuento

   
    visitantes = visitantes + 1
    total_descuentos = total_descuentos + descuento
    total_pagar = total_pagar + paga


    print(
        f"Visitante {visitantes} | Edad: {edad} | {tipo_nombre} "
        f"| Base: ${precio_base:.2f} "
        f"| Descuento: ${descuento:.2f} "
        f"| A pagar: ${paga:.2f}"
    )

    print("------------------------------------------------")


print("=== ticket ===")
print("visitantes cobrados:", visitantes)
print(f"total en descuentos: ${total_descuentos:.2f}")
print(f"total a pagar: ${total_pagar:.2f}")
print("------------------------------------------------")
print("¡Gracias por visitar el museo! :D")