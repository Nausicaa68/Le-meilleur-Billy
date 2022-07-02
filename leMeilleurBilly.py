
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
    moyPond /= len(billy)

    return moyPond


def determ_billy_class(classObjet):
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


def main_programme(maxAffichage):
    """
    affiche une liste triée des billy, du plus grand au plus petit
    indexOfParameter : index du paramètre servant au tri 
    Pour rappel -> format aBilly : [ [objets], [caract], classe, moyenneStat, mediane, moyennePonderee ]
    """

    all_Billy = []
    lesmeilleurs = []

    for key1 in caractObjet:
        for key2 in caractObjet:
            for key3 in caractObjet:
                if((key1 != key2) and (key1 != key3) and (key2 != key3)):
                    all_Billy.append(build_billy([key1, key2, key3]))

    print("len(all_Billy) :", len(all_Billy))

    # sort la liste en fct des moyennes
    print("Tri en fct des moyennes : ")
    all_Billy = sorted(all_Billy, key=lambda l: l[3], reverse=True)
    lesmeilleurs.append(all_Billy[0])
    for i in range(0, maxAffichage):
        print_Billy(all_Billy[i])
    print("\n")

    # sort la liste en fct des medianes
    print("Tri en fct des médianes : ")
    all_Billy = sorted(all_Billy, key=lambda l: l[4], reverse=True)
    lesmeilleurs.append(all_Billy[0])
    for i in range(0, maxAffichage):
        print_Billy(all_Billy[i])
    print("\n")

    # sort la liste en fct des moyennes ponderees
    print("Tri en fct des moyennes ponderees : ")
    all_Billy = sorted(all_Billy, key=lambda l: l[5], reverse=True)
    lesmeilleurs.append(all_Billy[0])
    for i in range(0, maxAffichage):
        print_Billy(all_Billy[i])
    print("\n")

    # les meilleurs
    print("Les meilleurs Billy sont :")
    for i in lesmeilleurs:
        print_Billy(i)


if __name__ == "__main__":
    main_programme(10)
