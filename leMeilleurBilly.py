
# "nom" : [hab, end, adr, cha, deg, arm, crit, PV], catégorie (1:arme, 2:equipement, 3:outils)

caractObjet = {
    "epee": [[4, 0, 0, 0, 0, 0, 0, 0], 1],
    "lance": [[3, 0, 1, 0, 0, 0, 0, 0], 1],
    "morgenstern": [[1, 1, 0, 0, 1, 0, 0, 0], 1],
    "arc": [[3, 0, 1, 0, 0, 0, 4, 0], 1],

    "cotemaille": [[-1, 1, -1, 0, 0, 2, 0, 0], 2],
    "marmite": [[0, 2, 0, 0, 0, 1, 0, 0], 2],
    "pamphlet": [[0, 0, 0, 4, 0, 0, 0, 0], 2],
    "kitdesoin": [[0, 0, 0, 1, 0, 0, 0, 0], 2],

    "fourche": [[1, 3, 0, 0, 0, 0, 0, 0], 3],
    "dague": [[1, 0, 0, 0, 0, 0, 6, 0], 3],
    "kitescalade": [[0, 0, 1, 0, 0, 0, 0, 0], 3],
    "sacgrain": [[0, 2, 0, 2, 0, 0, 0, 0], 3]
}

caractClasse = {
    "guerrier": [2, 0, 0, -1, 1, 0, 0, 0],
    "prudent": [-1, 0, 0, 2, 0, 0, 0, 0],
    "paysan": [0, 2, -1, 0, 0, 0, 0, 0],
    "debrouillard": [0, -1, 2, 0, 0, 0, 0, 0]
}

BILLY_DEBUT = [2, 2, 1, 3, 0, 0, 0, 0]
LES_CLASSES = ["guerrier", "prudent", "paysan", "debrouillard"]
PONDERATION_CARACT = [1, 1, 1, 1, 1, 1, 1, 1]


def calc_mediane(billy):
    """
    calcul de la médiane des caractéristiques d'un billy
    """
    mediane = 0

    buff = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(len(billy)):
        buff[j] += billy[j]

    buff.sort()
    if((len(buff) % 2) == 0):
        mediane = (buff[(int(len(buff)/2) - 1)] + buff[(int(len(buff)/2))]) / 2
    else:
        mediane = buff[(int(len(buff)/2) - 1)]

    return mediane


def calc_moyenne(billy):
    """
    calcul de la moyenne des caractéristiques d'un billy
    """
    moy = 0
    for j in range(len(billy)):
        moy += billy[j]
    moy /= len(billy)

    return moy


def calc_moyenne_ponderee(billy):
    """
    calcul de la moyenne pondérée des caractéristiques d'un billy
    """
    moyPond = 0
    for j in range(len(billy)):
        moyPond += (billy[j] * PONDERATION_CARACT[j])

    sommedesPond = 0
    for i in PONDERATION_CARACT:
        sommedesPond += i
    moyPond /= sommedesPond

    return moyPond


def determ_billy_class(classObjet):
    """
    permet de déterminer la classe d'un Billy. 
    Prend en parametre un tableau contenant les valeurs désignant la catégorie d'un objet : (1:arme, 2:equipement, 3:outils)
    """
    nbArme = 0
    nbEquip = 0
    nbOutil = 0

    for i in classObjet:
        if(i == 1):
            nbArme += 1
        elif(i == 2):
            nbEquip += 1
        elif(i == 3):
            nbOutil += 1
        else:
            print("error")
            return 0

    #print(nbArme, nbEquip, nbOutil)

    if(nbArme >= 2):
        return LES_CLASSES[0]
    elif(nbEquip >= 2):
        return LES_CLASSES[1]
    elif(nbOutil >= 2):
        return LES_CLASSES[2]
    else:
        return LES_CLASSES[3]


def build_billy(objets):

    newBilly = [0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(len(newBilly)):
        newBilly[j] += BILLY_DEBUT[j]

    # ajout des caracts liées aux objets
    for i in objets:
        for j in range(len(newBilly)):
            newBilly[j] += caractObjet[i][0][j]

    # détermine la classe de billy
    classedeBilly = determ_billy_class(
        [caractObjet[objets[0]][1], caractObjet[objets[1]][1], caractObjet[objets[2]][1]])

    # ajout des caracts liées a la classe
    for j in range(len(newBilly)):
        newBilly[j] += caractClasse[classedeBilly][j]

    # ajout des PV
    newBilly[7] = 3 * newBilly[1]

    # format aCompleteBilly : [ [objets], [caract], classe, moyenneStat, mediane, moyennePonderee ]

    # calcul de la moyenne
    moyenne = calc_moyenne(newBilly)

    # calcul de la médiane
    mediane = calc_mediane(newBilly)

    # calcul de la moyenne pondérée
    moyennePond = calc_moyenne_ponderee(newBilly)

    aCompleteBilly = [objets, newBilly,
                      classedeBilly, moyenne, mediane, moyennePond]
    # print(aCompleteBilly)

    return aCompleteBilly


def print_Billy(aBilly):
    """
    format aBilly : [ [objets], [caract], classe, moyenneStat, mediane, moyennePonderee ]
    """

    print("Ce Billy est équipé de", aBilly[0], "C'est un", aBilly[2])
    print("Caract complète :",
          aBilly[1], "  Moyenne :", aBilly[3], "  Moyenne pondérée :", aBilly[5], "  Mediane :", aBilly[4])
    print()


def triParametre(parametreName, parametreIndex, all_Billy, lesmeilleurs, maxAffichage):
    # sort la liste en fct du parametre
    print("Tri en fonction des", parametreName, ": ")
    all_Billy = sorted(
        all_Billy, key=lambda l: l[parametreIndex], reverse=True)
    lesmeilleurs.append(all_Billy[0])
    for i in range(0, maxAffichage):
        print_Billy(all_Billy[i])
    print("\n")


def main_programme(maxAffichage):
    """
    affiche une liste triée des billy, du plus grand au plus petit
    indexOfParameter : index du paramètre servant au tri 
    Pour rappel -> format aBilly : [ [objets], [caract], classe, moyenneStat, mediane, moyennePonderee ]
    """

    all_Billy = []
    lesmeilleurs = []

    allKeys = list(caractObjet.keys())

    for i in range(0, len(allKeys)):
        for j in range(i+1, len(allKeys)):
            for k in range(j+1, len(allKeys)):
                # if((key1 != key2) and (key1 != key3) and (key2 != key3)):
                all_Billy.append(build_billy(
                    [allKeys[i], allKeys[j], allKeys[k]]))

    #print("len(all_Billy) :", len(all_Billy))

    triParametre("moyennes", 3, all_Billy, lesmeilleurs, maxAffichage)
    triParametre("médianes", 4, all_Billy, lesmeilleurs, maxAffichage)
    triParametre("moyennes pondérées", 3, all_Billy,
                 lesmeilleurs, maxAffichage)

    # affichage des meilleurs pour chaque tri
    lesTris = ["moyennes", "médianes", "moyennes pondérées"]
    print("Les meilleurs Billy sont :\n")
    for i in range(len(lesmeilleurs)):
        print("En fonction des", lesTris[i], ":")
        print_Billy(lesmeilleurs[i])
        print("")


if __name__ == "__main__":
    main_programme(4)
