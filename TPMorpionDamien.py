# Morpion Damien Fernandes SN1
import random

def afficher_tableau(tableau):
    for ligne in tableau:
        print(" | ".join(ligne))
        print("-" * 10)

def verifier_victoire(tableau, symbole):
    # Vérification des lignes et des colonnes
    for i in range(3):
        if all([case == symbole for case in tableau[i]]) or \
           all([tableau[j][i] == symbole for j in range(3)]):
            return True
    
    # Vérification des diagonales
    if (tableau[0][0] == tableau[1][1] == tableau[2][2] == symbole) or \
       (tableau[0][2] == tableau[1][1] == tableau[2][0] == symbole):
        return True

    return False

def mouvement_ordi(tableau, symbole):
    # Vérification des lignes et des colonnes pour bloquer le joueur
    for i in range(3):
        # Vérification des lignes
        if tableau[i].count(symbole) == 2 and tableau[i].count(" ") == 1:
            return i, tableau[i].index(" ")
        
        # Vérification des colonnes
        col = [tableau[j][i] for j in range(3)]
        if col.count(symbole) == 2 and col.count(" ") == 1:
            return col.index(" "), i

    # Vérification des diagonales
    if (tableau[0][0] == tableau[1][1] == symbole and tableau[2][2] == " ") or \
       (tableau[0][2] == tableau[1][1] == symbole and tableau[2][0] == " "):
        if tableau[0][0] == " ":
            return 0, 0
        elif tableau[0][2] == " ":
            return 0, 2
        elif tableau[2][0] == " ":
            return 2, 0
        else:
            return 2, 2

    # Si aucune situation critique n'est détectée, jouer aléatoirement
        
    return random.choice([(i, j) for i in range(3) for j in range(3) if tableau[i][j] == " "])

def morpion():
    while True:
        tableau = [[" " for _ in range(3)] for _ in range(3)]
        joueur = "X"
        tour = 0

        while tour < 9:
            afficher_tableau(tableau)
            print("Tour du joueur", joueur)

            if joueur == "X":
                while True:
                    try:
                        ligne = int(input("Entrez le numéro de ligne (1, 2, 3) : ")) - 1
                        colonne = int(input("Entrez le numéro de colonne (1, 2, 3) : ")) - 1
                        if ligne not in [0, 1, 2] or colonne not in [0, 1, 2]:
                            raise ValueError("Les valeurs doivent être 1, 2 ou 3.")
                        break
                    except ValueError as e:
                        print(e)
                        print("Veuillez entrer des valeurs valides.")
            else:
                ligne, colonne = mouvement_ordi(tableau, "X")

            if tableau[ligne][colonne] == " ":
                tableau[ligne][colonne] = joueur
                if verifier_victoire(tableau, joueur):
                    print("Le joueur", joueur, "a gagné !")
                    afficher_tableau(tableau)
                    break
                joueur = "O" if joueur == "X" else "X"
                tour += 1
            else:
                print("Cette case est déjà occupée !")

        if tour == 9:
            print("Match nul !")
       
        rejouer = input("Voulez-vous rejouer ? (oui/non) : ")
        if rejouer.lower() != "oui":
            break

morpion()