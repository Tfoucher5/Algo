def afficher_longueur_mot(mot):
    longueurs = []
    while mot.lower() not in ["stop"]:
        longueur = len(mot)
        longueurs.append(longueur)
        mot = input("Entrez un mot (écrire STOP pour arrêter): ")

    total_lettres = sum(longueurs)
    print("Nombre total de lettres:", total_lettres)
    print("Programme terminé.")

premier_mot = input("Entrez un mot (écrire STOP pour arrêter): ")

afficher_longueur_mot(premier_mot)