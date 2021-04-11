variable = open("texte.txt")
txt = variable.read().replace("\n", "")
x = 0
L = txt.split()
motsmaj = []
nptemp = []
abc = 'abcdefghijklmnopqrstuvwxyz'
ponctuation = '.!?;:'
ABC = abc.upper()
# je créer une liste propre en enlevant les '.' et ',' pour pouvoir compter les noms propre
nouvelleListe = []
listeVide = []
paquetNomsPropre = []
textePropre = []
# je filtre les virgules dans le texte
for string in L:
    new_string = string.replace(",", "")

    nouvelleListe.append(new_string)
# je filtre les points dans le texte
for string in nouvelleListe:
    new_string = string.replace(".", "")

    textePropre.append(new_string)

# je récupere les noms propre
for k in range(len(L)) :
  if L[k][0] in ABC :
    # motsmaj = tout les mots en majuscule
    motsmaj.append(L[k])
    if not(L[k-1][-1] in ponctuation):
      #nptemp c'est les mots en majuscule qui ne précédent pas une ponctuation
      nptemp.append(L[k])



#je nettoie le premier packet de noms propre

for string in nptemp:
    new_string = string.replace(",", "")

    listeVide.append(new_string)

for string in listeVide:
    new_string = string.replace(".", "")

    paquetNomsPropre.append(new_string)

# je check si un de mes noms propre correspond a un début de phrase et je le compte
for mot in textePropre :
  if mot in paquetNomsPropre :
    x += 1

# enlever les doublons de nom propres 
paquetNomsPropre = list(set(paquetNomsPropre))

print("il y a ",x," noms propre \n")
print("voici le paquet de noms propre récupérer : \n \n",paquetNomsPropre)


