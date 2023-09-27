from tkinter import Variable


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
else:
    print("Respuesta incorrecta")

    