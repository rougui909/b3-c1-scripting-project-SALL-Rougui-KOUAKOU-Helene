import csv

def additionner(x, y):
    result = x + y
    return result


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