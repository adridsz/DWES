import random


p = 0
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
    
    print(ca[adivinanza])
    respuesta=input()
    v+=1
    if v==3:
        break

while True:
    respuesta = input("Introduce la respuesta(A,B o C):" ).lower()
    if respuesta in ["a", "b", "c"]:
        break

else:
    print("Respuesta incorrecta")
    puntos-=5
print("Obtuviste ",puntos," de 30 posibles")