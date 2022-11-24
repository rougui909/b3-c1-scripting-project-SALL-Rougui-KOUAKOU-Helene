import csv
<<<<<<< HEAD

with open('conso-annuelles_v1.csv', 'r', newline='', encoding='latin-1') as in_file, open ('conso-clean.csv', 'w', newline='', encoding='latin-1') as out_file:
    #ouvrir le fichier conso-annuelles.csv en entrée en mode lecture et crétation du fichier de sortie conso-clean.csv en mode écriture
    #tableau=[]
    lire=csv.reader(in_file) #creation de l'objet csv lire à partir du fichier d'entrée
    ecrire=csv.writer(out_file) #creation de l'objet csv écrire à partir du fichier de sortie
    #print('', end='\n')
    #print('Affichage des lignes du tableau', end='\n')
    for ligne in lire: #iterer les lignes de notre fichier d'entrée ou chaque ligne sera une liste Python
        #if any(field.strip() for field in ligne):
            #print(ligne)
            #tableau=[]
        #if ligne.strip('\n') != '; ;':
            ecrire.writerow(ligne)
