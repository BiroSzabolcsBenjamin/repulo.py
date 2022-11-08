import random
lista = []

#a
for i in range (20):
    lista.append(random.randint(0, 9)) 

print("Mérési eredmény: ", ', '.join(map(str, lista))) #Zárójel nélkül irja ki

#b
print("Legmagasabb pont: ",max(lista))

#c
lista = sorted(lista)
while lista[0] == 0:
    lista.remove(lista[0])

kül = max(lista) - min(lista)
print("Külömbség: ",kül)

#d
víz = 0
for i in lista:
    if i == 0:
        víz += 1

szarazfold = 20 - víz

if szarazfold > 10:
    print("Több a szárazföldi terület.")
elif víz > 10:
    print("Több a vizes terület.")
else:
    print("Egyforma a terület elosztás.")