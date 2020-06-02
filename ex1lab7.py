#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 1 lab 7

def histogramme(texte):
    lettres = {}
    for c in texte:
        lettres[c]=lettres.get(c,0) + 1
    return lettres

t = "bonjour"

d = histogramme(t)

lettres_triees = list(d.items())
lettres_triees.sort()
print(lettres_triees)
