import csv

tableau = [] #déclaration de tableau vide pour les données 
with open('conso-annuelles_v1.csv', 'r') as in_file, open ('conso-clean.csv', 'w') as out_file:
    #ouvrir le fichier conso-annuelles.csv en entrée en mode lecture et crétation du fichier de sortie conso-clean.csv en mode écriture
    lire=csv.reader(in_file, delimiter = ';') #creation de l'objet csv lire à partir du fichier d'entrée
    ecrire=csv.writer(out_file, delimiter = ';') #creation de l'objet csv écrire à partir du fichier de sortie
    for ligne in lire:
        tableau.append(ligne)
        if ligne[2] != '' and ligne[3] != '' and ligne[4] != '': #suppression des lignes avec cellules vides
            ecrire.writerow(ligne)
    for d in tableau:
        print (d)
