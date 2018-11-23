teclado = input("Introduce una contraseña:")
boolean = (0)
lista = list(teclado)
listmayus = len([c for c in  teclado if c.isupper()])
listminus = len([c for c in  teclado if c.islower()])
listnum = len([c for c in  teclado if c.isdigit()])
print(listnum)
print(listmayus)
print(listminus)
while boolean == 0:
    if len(teclado) < 12:
         print("La contraseña es demasiado corta.")
         boolean = (1)
    elif listnum > 0 & listmayus == 0 & listminus == 0 & teclado.isalpha() == False :
        print("Buena contraseña")
        boolean = (1)
    else:
        print("Mala contraseña")
