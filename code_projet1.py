import csv

    

tableau = [] #déclaration de tableau vide pour les données 
with open('conso-annuelles_v1.csv', 'r') as in_file, open ('conso-clean.csv', 'w') as out_file:
    #ouvrir le fichier conso-annuelles.csv en entrée en mode lecture et crétation du fichier de sortie conso-clean.csv en mode écriture
    lire=csv.reader(in_file, delimiter = ';') #creation de l'objet csv lire à partir du fichier d'entrée
    ecrire=csv.writer(out_file, delimiter = ';') #creation de l'objet csv écrire à partir du fichier de sortie
    for ligne in lire:
        tableau.append(ligne) #ajout des lignes
        if ligne[2] != '' and ligne[3] != '' and ligne[4] != '': #suppression des lignes avec cellules vides
            del ligne[1] #supprimer la colonne ID logement 
            ecrire.writerow(ligne) #ecris dans le fichier conso-clean
    #affiche le fichier conso-annuelles
    for d in tableau:
        print (d)

    #Addition des consommations

    t=[]
    x=[]

    t.append(float(ligne[2])) 
    x.append(float(ligne[3])) 
     
    print(t)
    print(x)


    with open('conso-annuelles_v1.csv') as file:
            total = sum(float(ligne[2]) and float(ligne[3]) for ligne in csv.reader(file))

    #Tri par type et Regroupement dans l'ordre décroissant
    lignes_ordonnees = sorted(csv.reader, key=lambda test: ecrire, reverse=True)

    with open('conso-annuelles-v1.csv', 'w', newline='') as file:

                    ecrire = csv.writer(file, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for ligne in lignes_ordonnees:
                        ecrire.writerow(ligne)
    for ligne in lignes_ordonnees:
                    print(ligne)
            

    #Tri par consommation et Regroupement par consommation dans l'ordre décroissant
    lignes_ordonnees = sorted(csv.reader, key=lambda test: ecrire, reverse= True)

    with open('conso-annuelles-v1.csv', 'w', newline='') as file:

                    ecrire = csv.writer(file, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    for ligne in lignes_ordonnees:
                        ecrire.writerow(ligne)
    for ligne in lignes_ordonnees:
                   print(ligne)
