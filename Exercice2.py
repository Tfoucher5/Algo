def afficher_longueur_mot(mot):        
    while mot != "STOP" or "Stop" or "stop":
        longueur = len(mot)
        print("Le mot", mot, "contient", longueur, "lettres.")
        mot = input("Entrez un mot (écrire STOP pour arrêter): ")
    print("Programme terminé.")

# Demander le premier mot à l'utilisateur
premier_mot = input("Entrez un mot (écrire STOP pour arrêter): ")

# Appeler la fonction avec le premier mot
afficher_longueur_mot(premier_mot)