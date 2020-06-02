#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 2 lab 7

def histo_n(tuple1):
    h = {}
    for i in tuple1:
        h[i] = h.get(i,0) + 1
    return h




t = (1,2,-3,3,4,-3,3,3)
d = histo_n(t)

liste1 = list(d.items())
liste1.sort()
print(liste1)
