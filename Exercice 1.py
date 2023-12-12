n = input("Entrez un mot: ")

def etoile(mot):
    mot_fin = len(mot) * "*"
    return mot_fin

mot_resultat = etoile(n)
print(mot_resultat)