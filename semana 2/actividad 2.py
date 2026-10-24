#este es el bueno
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
print("tipo 1: adulto mayor, 12% de descuento")
print("tipo 2: estudiante, 10% de descuento")
print("tipo 3: maestro, 10% de descuento")
print("tipo 4: ninguno, sin descuento")
print("------------------------------------------------")

# Pedir la edad
while True:
    try:
        edad = int(input("escribe tu edad: "))

        if edad < 0 or edad > 110:
            print("edad no válida, escribe una edad entre 0 y 110")
        else:
            break

    except ValueError:
        print("error, escribe tu edad con números, no con letras")

# Revisar el precio del boleto
if edad < 3:
    print("tu boleto es gratis")

else:
    # Pedir el tipo de visitante
    while True:
        try:
            tipo = int(input("¿qué tipo de descuento te aplica? ¿1, 2, 3 o 4? "))

            if tipo >= 1 and tipo <= 4:
                break
            else:
                print("opción no válida, escribe un número del 1 al 4")

        except ValueError:
            print("error, escribe el tipo de descuento con números, no con letras")

    # Mostrar el precio del boleto
    if edad >= 3 and edad <= 17:
        print("tu boleto cuesta $30")
    elif edad >= 18:
        print("tu boleto cuesta $45")

    # Mostrar el descuento
    if tipo == 1:
        print("tu descuento es del 12%")
    elif tipo == 2:
        print("tu descuento es del 10%")
    elif tipo == 3:
        print("tu descuento es del 10%")
    elif tipo == 4:
        print("tu descuento es del 0%")

# Finalizar el programa
siono = input("escribe 'fin' si ya quedó bien tu ticket: ")

if siono == "fin":
    print("toma tu ticket y llevalo a taquilla, se te pedirá comprobante para tu descuento, ¡gracias por visitar el museo! :D")