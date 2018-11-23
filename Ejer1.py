#Programa created by Joaquin Diaz y Sebastian Tangarife
#Love Python
import random
numero=random.randrange(10)
boolean = (0)
print(numero)
teclado = input("Introduce un numero:")
teclado = int(teclado)
while boolean == 0:
   if(teclado==numero):
        print("Acertaste")
        boolean = (1)
   elif (teclado>numero):
        print("El numero es mayor")
        boolean = (0)
        teclado = input("Introduce un numero:")
        teclado = int(teclado)
   elif(teclado<numero):
       print("El numero es menor")
       boolean = (0)
       teclado = input("Introduce un numero:")
       teclado = int(teclado)



