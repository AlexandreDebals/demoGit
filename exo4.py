'''
*** Exo 4: somme de saisies ***
Créer un programme demandant à l'utilisateur se saisir
un chiffre. Tant que l'utilisateur ne saisit pas la valeur "0",
on lui redemande la saisie d'un chiffre.
En sortie de boucle, on affichera la somme des valeurs saisies ainsi qu'un
récapitulatif des valeurs saisies
Exemples de valeurs saisies par l'utilisateur:
15
2
3
0
=> Somme des valeurs saisies: 20 (15,2,3)
'''
print("*** EXO 4: somme de saisies ***")

valeur = int(input("entrez un chiffre"))
somme = 0

historique = []

while valeur != 0:
    
    historique.append(valeur)
    somme += valeur
    valeur = int(input("entrez un chiffre"))

    
print("Somme des valeurs saisie : ",somme,"historique des valeurs : ",historique)