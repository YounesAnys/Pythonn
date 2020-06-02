#Auteur : Younes Anys
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numero d'étudiant : 300145843")

#Exercice 4 lab 7

def move_zeros(lst):

    tmp = [0]*len(lst)
    index_tmp = 0

    for i in range(len(lst)):
        if (lst[i]!=0):
            tmp[index_tmp] = lst[i]
            index_tmp = index_tmp + 1
    return tmp

x = [1,0,3,0,0,5,7]
print(x)
y = move_zeros(x)
print(x,y)
