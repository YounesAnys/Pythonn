#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 3 lab 7

def somme_de_trois(tuple1):
    res = False

    i = 0
    somme = 0

    while (i < len(tuple1)-2):
        somme = somme + tuple1[i] + tuple1[i+1] + tuple1[i+2]
        if (somme == 0):
            res = True
            break
        i + i + 1
    return res

        



t = (1,2,-3,4,-1,3)
print(somme_de_trois(t))



