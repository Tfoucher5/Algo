def demander_nombres():
    nombres = []
    somme = 0
    
    while True:
        nombre = float(input("Entrez un nombre (0 pour arrêter) : "))
        
        if nombre == 0:
            break
        
        nombres.append(nombre)
        somme += nombre
        
        if somme >= 100:
            break
    
    return nombres

def demander_indices(taille):
    while True:
        index1 = int(input(f"Entrez le premier index (entre 0 et {taille - 1}) : "))
        index2 = int(input(f"Entrez le deuxième index (entre 0 et {taille - 1}) : "))
        
        if 0 <= index1 < taille and 0 <= index2 < taille:
            return index1, index2
        else:
            print("Indices invalides. Veuillez réessayer.")

def main():
    nombres_saisis = demander_nombres()
    print("Nombres saisis :", nombres_saisis)
    
    index1, index2 = demander_indices(len(nombres_saisis))
    
    somme_indices = nombres_saisis[index1] + nombres_saisis[index2]
    
    print(f"La somme des valeurs aux indices {index1} et {index2} est : {somme_indices}")

if __name__ == "__main__":
    main()