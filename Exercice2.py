def afficher_longueur_mot(mot):
    longueurs = []
    while mot.lower() not in ["stop"]:
        longueur = len(mot)
        longueurs.append(longueur)
        mot = input("Entrez un mot (écrire STOP pour arrêter): ")
    print(longueurs)
    print("Programme terminé.")

premier_mot = input("Entrez un mot (écrire STOP pour arrêter): ")

afficher_longueur_mot(premier_mot)