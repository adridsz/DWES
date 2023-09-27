from operaciones import suma, resta, multiplicacion, division

while True:
    num=int(input("Introduce un numero "))
    num2=int(input("introduce otro numero "))
    while True:
        print("1- Suma")
        print("2- Resta")
        print("3- Multpicplicacion")
        print("4- Division")
        opcion=int(input("¿Que deseas hacer? "))
        if opcion==1 or opcion==2 or opcion==3 or opcion==4:
            break
    if opcion==1:
        print(suma(num, num2))
    elif opcion==2:
        print(resta(num, num2))
    elif opcion==3:
        print(multiplicacion(num, num2))
    elif opcion==4:
        print(division(num, num2))
    while True:
        opcion=input("¿Deseas realizar otra operación? (S/N) ").lower()
        if opcion=="s" or opcion=="n":
            break
    if opcion=="n":
        break