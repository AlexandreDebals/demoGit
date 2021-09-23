'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniro-report.txt" 
affichant les informations suivantes:
Nom du film le mieux noté
Nombre de films entre 2000 et 2010
'''
print("*** EXO 7: CSV De Niro ***")

import os,shutil

f= open("deniro.csv","r")
content = f.read() #lecture et stockage du contenu
f.close()


rows = content.splitlines()
print(rows)
anneeSortie = 1 #colone 1 dans fichier deniro
note =  2 #colone 2 dans fichier deniro
nombreFilmCorespondant = 0
filmLeMieuxNote = ""
note =[ 0, 0 ]
nomFilm =["rien","rien"]
valeurmax = 0 #indice colone meilleure note

for r in rows[1:] :
    cols = r.split(",") #séparateur de colonne
    anSortie= cols[0]
    anSortie = int(anSortie)
    #print(anSortie)
    if anSortie > 2000 and anSortie <=2010  :
        nombreFilmCorespondant +=1
print("nombre film sortie entre 2000 et 2010 : ",nombreFilmCorespondant)

for r in rows[1:] :
    cols = r.split(",") #séparateur de colonne    
    note.append( int(cols[1]))
    nomFilm.append(str(cols[2]))
    #print(nomFilm)
    valeurmax = note.index(max(note))
    #print(note)
    #print(note.index(max(note)))
    filmLeMieuxNote= nomFilm[valeurmax]
    #print(filmLeMieuxNote)


print("le film le mieux noté est",filmLeMieuxNote)


extensions = ["txt","log","jason","js","exe"]
targetdir = "tmp/"
filesNames= ["script","demo","test","exemple","new"]

'''
filename="deniro-report.txt"
f= open(filename,"w")
f.write("nombre film sortie entre 2000 et 2010 : ")
f.write(str(nombreFilmCorespondant))
f.write(" le film le mieux note est ")
f.write(filmLeMieuxNote)
f.close()
print("creation du fichier %s" %filename)
'''