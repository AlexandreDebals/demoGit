'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png
Le fichier missing.png devra être ignoré
'''
print("*** EXO 5: flags => flagsBis ***")

import os

targetDir = os.mkdir("/exos/flagsBis")

def rename(file,extention="png") :
    f= open(file,"w")
    f=file[:1].upper()+"."+"extention"
    f.close()
    return f


for i in os.path("/exos/flags") :
    try:
        newFile = targetDir + rename(i)
    except missing.png :
        exit()




