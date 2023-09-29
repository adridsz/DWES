import random


pm=0
pj=0
v=0
j=0

while v<5:
    j=int(input("Elige lo que vas a jugar (1- Piedra  2- Papel  3- Tijera) "))
    m = random.randint(1,3)
    print("La maquina saca ",m)
    if j==m:
        print("¡Empate! Esta jugada no la contaremos")
    elif j == 2 and m == 3 or j == 3 and m == 1 or j==1 and m==2:
        print("La maquina gano")
        pm+=1
        v+=1
    elif j == 2 and m == 1 or j == 3 and m== 2 or j==1 and m==3:
        print("Ganaste")
        pj+=1
        v+=1
    print("Marcador: Persona ",pj," Maquina ",pm)
print("Quedasteis ",pj, " a ",pm)
if pj>pm:
    print("¡Ganaste!")
else:
    print("¡Perdiste!")