#1.pedir al usurio que responda una pregunta.

print("bienvenido, usuario")
print("es usted culpable si o no")
respuesta =input()

if respuesta == "si":
    print("debe ir a la carcel")
else:
    print("debe regresar a su casa")
print(" muchas gracias por asistir")


#2.Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no

edad= int(input("ingrese su edad:"))

if edad <18:
    print("eres menor de edad")
else:
    print("eres mayor de edad")