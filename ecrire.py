import csv
with open('conso-annuelles_v1.csv', 'w',  newline='') as csvfile:
    ecrire = csv.writer(csvfile, delimiter=' ', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
    ecrire.writerow(['Spam'] * 5 + ['Baked Beans'])
    ecrire.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])