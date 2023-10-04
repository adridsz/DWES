import random


puntos = 0
v = 0
a = {
    1: "La A, anda. La B, besa. La C, reza. ¿Qué fruta es esa? (A- Pera  B- Cereza  C- Manzana)",
    2: "Soy bonito por delante, algo feo por detrás, me transformo a cada instante, ya que imito a los demás. (A- Espejo  B- Titere  C- Farola)",
    3: "Ruedo y ruedo, y en los bolsillos me quedo.(A- Cartera  B- Llaves  C- Moneda)"
}

ca=list(a.keys())
while True:
    adivinanza = random.sample(ca, 1) [0]
    ca.remove(adivinanza)
    
    print(a[adivinanza])
    while True:
        respuesta = input("Introduce la respuesta(A,B o C): ").lower()
        if respuesta in ["a", "b", "c"]:
            break
    v+=1
    if adivinanza==1:
        if respuesta=="b":
            print("La respuesta es correcta")
            puntos+=10
        else:
            print("Respuesta incorrecta")
            puntos-=5
    elif adivinanza==2:
        if respuesta=="a":
            print("La respuesta es correcta")
            puntos+=10
        else:
            print("Respuesta incorrecta")
            puntos-=5
    elif adivinanza==3:
        if respuesta=="c":
            print("La respuesta es correcta")
            puntos+=10
        else:
            print("Respuesta incorrecta")
            puntos-=5
    if v==2:
        break
print("Obtuviste ",puntos," de 20 posibles")