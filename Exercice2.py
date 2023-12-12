def afficher_longueur_mot(mot):
    longueur_tab = []
    while mot.lower() not in ["stop"]:
        longueur = len(mot)
        longueur_tab.append(longueur)
        mot = input("Entrez un mot (écrire STOP pour arrêter): ")
    print(longueur_tab)
    print("Programme terminé.")

premier_mot = input("Entrez un mot (écrire STOP pour arrêter): ")

afficher_longueur_mot(premier_mot)