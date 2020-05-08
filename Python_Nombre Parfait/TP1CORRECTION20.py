# Exo 1 nombres parfaits

def parfait(n):
    # Teste si n est parfait
    somme = 1
    for i in range(n//2,1,-1):
        if n % i == 0:
            somme = somme + i
    return n == somme
    
# Remarque : on parcourt les entiers de n/2 Ã  1, en decrementant
# i Ã  chaque iteration
# range(debut,fin,pas) parcours de debut Ã  fin
# en ajoutant pas (-1) Ã  chaque iteration
# ce n'est pas la peine de parcourir de 1 Ã  n, 1 Ã  n/2 suffit
# n % i donne le reste de la division de n par i
# return n == somme : la valeur retournee est un boolean resultat
# de la comparaison entre n et somme
# somme, i et n sont des variables locales

# nombres parfaits inferieurs Ã  n
# plusieurs versions

import sys
sys.setrecursionlimit(1500)


def imp_parfait(n):
    "Liste l'ensemble des nombres parfait de 1 Ã  n"
    if n == 1:
        print (1)
    else:
        if parfait(n):
            print (n)
        imp_parfait(n-1)


# Exo 2: Tri par selectiton 

def echange(l,i,j):
    t=l[i]
    l[i]=l[j]
    l[j]=t

def tri_selection(l):

    for i in range(len(l)-1):

        mini=i

        for j in range(i+1,len(l)):

            if l[j]<l[mini]:

                mini=j

        echange(l,i,mini)
    return l
