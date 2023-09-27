puntos = 0

print("La A, anda. La B, besa. La C, reza. ¿Qué fruta es esa?")
print("A- Pera")
print("B- Cereza")
print("C- Manzana")
while True:
    respuesta = input("Introduce la respuesta(A,B o C):" ).lower()
    if respuesta=="a" or respuesta=="b"or respuesta=="c":
        break
if respuesta=="b":
    print("La respuesta es correcta")
    puntos+=10

else:
    print("Respuesta incorrecta")
    puntos-=5

print("Soy bonito por delante, algo feo por detrás, me transformo a cada instante, ya que imito a los demás. ")
print("A- Espejo")
print("B- Titere")
print("C- Farola")
while True:
    respuesta = input("Introduce la respuesta(A,B o C):" ).lower()
    if respuesta=="a" or respuesta=="b"or respuesta=="c":
        break
if respuesta=="a":
    print("La respuesta es correcta")
    puntos+=10

else:
    print("Respuesta incorrecta")
    puntos-=5

print("Ruedo y ruedo, y en los bolsillos me quedo.")
print("A- Cartera")
print("B- Llaves")
print("C- Moneda")
while True:
    respuesta = input("Introduce la respuesta(A,B o C):" ).lower()
    if respuesta=="a" or respuesta=="b"or respuesta=="c":
        break
if respuesta=="c":
    print("La respuesta es correcta")
    puntos+=10

else:
    print("Respuesta incorrecta")
    puntos-=5
print("Obtuviste ",puntos," de 30 posibles")