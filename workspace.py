import numpy as np 
import random



dias = {0:"Lunes",1:"Martes",2:"Miercoles",3:"Jueves",4:"Viernes",5:"Sabado",6:"Domingo"}

def generate():
    a = np.random.randint(18,34,(5,7))
    a[4][3:] = 0
    return a
 

def prom(array_):
    for semana_, semana in enumerate(array_):
        if semana_ != 4:
            yield np.mean(semana)
        else:
            yield np.mean(semana[:3])

a = generate()
print(a)
for prom_resul in prom(a):
    print(prom_resul)

#Max
print(np.max(a))
print(np.max(a[0,7][1,7][2,7][3,7],[4,7],))

#Min
a[4][3:] = 111110
print(np.min(a))
a[4][3:] = 0
#Cambiar valores
quest = input("Desea cambiar alguna temperatura del calendario. Yes/No")
quest.lower()
if quest == no:
    #return final
#else:
    quest2 = int(input("Digte el día del mes que desea editar: "))
    quest2 = quest2 - 1


cont = 0
for i in range(5):
    for j in range(7):
        cont += 1 
        if (cont == quest2):
            a[i][j]=int(input("Ingrese el nuevo valor: "))


print(a)