print("Bienvenido al museo de antropoligía e historia de google collab :D")
print("vamos a comprar tu boleto")
print("ofrecemos distintos precios y descuentos")
print("son los siguientes:")
print

funcionamiento = True

while funcionamiento == True:
  edad = int(input("escribe tu edad: "))
  if edad > 110:
    print("edad no válida, vuelve a correr el programa y escribe una edad válida")
  funcionamiento = False
else:
  tipo = int(input("¿qué tipo de visitante eres? ¿1, 2, 3 o 4?"))