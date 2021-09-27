'''
*** EXO 8: Health Check *** (permet de vérifier qu'une application ou serveur web répond (le status code renvoyé))
Créer un programme qui, à partir du fichier websites.txt
vérifie que chacun des sites listées répond (status code avec requests)
à raison d'une requête toutes les n secondes (avec du .append "a" pour ne pas écraser. périodicité avec un module nommé time, la fonction sleep permet de
bloquer l'utilisation du programme pendant n secondes.)
la périodicité sera fournie en entrée par l'utilisateur (input : Tout les combien de temps voulez-vous check les sites web")
On produira en sortie un fichier de log ('healthCheck.log') qui contiendra :
    - la date de la requête de vérification
    - l'url interrogée
    - le status code obtenu ou une indication d'erreur en cas de non réponse
'''
"Boucle infini avec while true et l'isntruction break, check sur 5min ou s'autostop sur une certaine échéance"

print("*** EXO 8: Health Check ***")

# votre code ici
import requests
import datetime
import time

nombreTest = int(input("Nombre de vérification de site web ? "))
periodicTime = int(input("periode de vérification ? "))
for i in range(nombreTest):
    while True :
        with open("files/websites.txt", "r") as webSites :
            lignes = webSites.read().splitlines()
            #print(lignes)
            for site in lignes :
                try :
                    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    response = requests.get(site)
                    #print(response)
                    with open("files/healthCheck.log", "a") as logFile :
                        logFile.write(str(date) + " : " + site + " : " + "Etats du site : " + str(response.status_code) + "\n")
                except :
                    with open("files/healthCheck.log", "a") as logFile :
                        logFile.write("=> Erreur : pas de réponse du site web" + "\n")
        time.sleep(periodicTime)
        print(f"La vérification n°{i+1} a été effectuée.")
        break