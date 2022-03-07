import time

c = time.time()
dico = {}
for i in range(10000):
    dico["VAR"+str(i)] = "MORIS" + str(i)
c1=time.time() - c

c = time.time()
liste = []
for i in range(10000):
    liste.append("MORIS" + str(i))
c2=time.time() - c

c = time.time()
for i in range(10000):
    print(dico["VAR"+str(i)])
c3=time.time() - c

c = time.time()    
for i in range(10000):
    print(liste[i])
c4=time.time() - c    

print("Création DICO : " + str(c1))
print("Création LISTE : " + str(c2))
print("Parcours DICO : " + str(c3))
print("Parcours LISTE : " + str(c4))


# -- Création DICO : 0.020943641662597656
# -- Création LISTE : 0.00897359848022461
# -- Parcours DICO : 3.3031725883483887
# -- Parcours LISTE : 3.3221213817596436    

input("Pause")