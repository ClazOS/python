from random import randint
from sys import exit

'''Implémentation python du jeu du Verger de Valentin'''

#Objets du jeu
faces_de = ["bleu","rouge","vert","jaune","panier","corbeau"]
arbre = {"prune(s)":4,"pomme(s) rouge(s)":4,"pomme(s) verte(s)":4,"poire(s)":4}
position_corbeau = 0
cases = 5
fini = False

#fonctions 
def lancer():
    '''Fonction simulant un lancer de dé à 6 faces du jeu. Retourne une des faces du dé du jeu.'''
    return faces_de[randint(0,5)]

def afficher(arbre,position_corbeau):
    '''Fonction affichant l’état du jeu : le contenu de l’arbre et la position du corbeau'''
    print("L’arbre contient :")
    for key in arbre:
        if arbre[key] > 0:
            print(arbre[key],key)
    print("Le corbeau est à", cases - position_corbeau,"cases du verger !")

def statut(arbre,position_corbeau):
    '''Fonction qui vérifie le statut du jeu et si la partie est finie'''
    fruits = 0
    for key in arbre:
        fruits += arbre[key]
    if fruits == 0:
        print("Bravo, vous avez battu le corbeau !")
        return True
    elif cases - position_corbeau == 0:
        print("Oh non, le corbeau a mangé tous les fruits")
        return True
    else:
        return False

def jouer_tour(arbre, position):
    '''fonction qui simule un tour de jeu, utilise la fonction lancer() et la fonction afficher()'''
    print("Vous lancez le dé")
    dé = lancer()
    print(dé," !")
    if dé == "panier":
        choix = input("Choisissez un fruit: \n1 pour prune\n2 pour pomme rouge\n3 pour pomme verte\n4 pour poire\n")
        while choix not in ["1","2","3","4"]:
            choix = input("Choisissez un fruit: \n1 pour prune\n2 pour pomme rouge\n3 pour pomme verte\n4 pour poire\n")
        dé = faces_de[int(choix) -1]
    if dé == "jaune":
        if arbre["poire(s)"] > 0:
            arbre["poire(s)"] -= 1
            print("Vous prenez une poire")
            return (arbre, position)
        else:
            print("Il n’y a plus de poires !")
            return (arbre, position)
    elif dé == "vert":
        if arbre["pomme(s) verte(s)"] > 0:
            arbre["pomme(s) verte(s)"] -= 1
            print("Vous prenez une pomme verte")
            return (arbre, position)
        else:
            print("Il n’y a plus de pommes vertes !")
            return (arbre, position)
    elif dé == "bleu":
        if arbre["prune(s)"] > 0:
            arbre["prune(s)"] -= 1
            print("Vous prenez une prune")
            return (arbre, position)
        else:
            print("Il n’y a plus de prunes !")
            return (arbre, position)
    elif dé == "rouge":
        if arbre["pomme(s) rouge(s)"] > 0:
            arbre["pomme(s) rouge(s)"] -= 1
            print("Vous prenez une pomme rouge")
            return (arbre, position)
        else:
            print("Il n’y a plus de pommes rouges !")
            return (arbre, position)
    elif dé == "corbeau":
        print("Oh non, le corbeau avance d’une case !")
        position += 1
        return (arbre, position)

while not fini:
    afficher(arbre, position_corbeau)
    print()
    arbre, position_corbeau = jouer_tour(arbre, position_corbeau)
    pause = input('Presser une touche pour continuer')
    fini = statut(arbre, position_corbeau)
