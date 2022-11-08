import random
Lmeres = []

#a
for i in range (20):
    #víz vagy szárazföld?
    terulet=random.randint(0,1)
    if (terulet==0):           #víz
        Lmeres.append(terulet)                                       # <-- jobb megoldás
    else:                      #különben szárazföld  
        Lmeres.append(random.randint(1,9))
    

print(Lmeres)
print("Legmagasabb hegy: ",max(Lmeres))


#nem 0 legalacsonyabb pont
minimum=9
for adat in Lmeres:
    if((adat!=0) and (adat<minimum)):
        minimum=adat

print("Legkisebb, ami nem 0: ",minimum)
print("Legmagasabb és legalacsonyabb közötti különbség:",max(Lmeres)-minimum)