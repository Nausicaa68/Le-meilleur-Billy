# Le-meilleur-Billy

Eh gamin ! Si tu t'es procuré *La Forteresse du chaudron Noir*, c'est certain, 

**TU**

**ES** 

**BILLY** 

**!!!**

Mais quel Billy es-tu ? Es-tu LE meilleur Billy ?

Moi, je suis un Billy informaticien. Et comme tout informaticien, j'informatise ! Il y a 3 objets à choisir, parmi 12. Rend toi compte, gamin, cela fait 12×11×10 combinaisons possibles, soit 1320. En sachant que chaque objet donne des caractéristiques différentes, qu'une classe a des capacités spécifiques et que certaines caractéristiques de Billy sont plus importantes que d'autres, quelles sont les *3 objets* à choisir pour avoir le meilleuuuuuuuuuuuuuur Billy !?

Voyons comment l'informatique peut nous aider.

## Modélisons nos informations

Premièrement, il faut modéliser nos données. Nous allons représenter un objet comme suit : 

```
"nom de l'objet" : [[hab, end, adr, cha, deg, arm, crit, PV], catégorie]
```

La catégorie est la suivante : 1 pour une arme, 2 pour un équipement, 3 pour un outil. Nous allons stocker tout cela dans un dictionnaire.

``` python
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
```

Faisons de même avec les classes. Considerons que chaque classe à des caractéristiques (bien que certains attribut de classes soient difficelement quantifiables comme la relance d'un dé pour le débrouillard). Cela nous permettra d'ajouter tous les points de chaque stat à la fin. 

``` python
caractClasse = {
    "guerrier": [2, 0, 0, -1, 1, 0, 0, 0],
    "prudent": [-1, 0, 0, 2, 0, 0, 0, 0],
    "paysan": [0, 2, -1, 0, 0, 0, 0, 0],
    "debrouillard": [0, -1, 2, 0, 0, 0, 0, 0]
}
```

## 1320 combinaisons, that's a lot

Comment parcourir ces 1320 combinaisons. Faisons une triple boucle for dont les intructions au bout ne s'exécute que si les trois objets sont différents (on ajoute un petit compteur pour voir) : 

``` python
count = 0
print(count)
for key1 in caractObjet:
        for key2 in caractObjet:
            for key3 in caractObjet:
                if((key1 != key2) and (key1 != key3) and (key2 != key3)):
                    # construire un Billy tout neuf
                    count += 1
print(count)
```

On obtient :

![image](https://user-images.githubusercontent.com/58084848/177019434-25af62c7-30f2-4cf5-80e2-a14f99aab082.png)

Cependant, effectuer cette combinaison nous induit à prendre plusieurs fois le même trio objet. On peut ainsi obtenir le trio "arc epee pamphlet", puis obtenir plus loin le trio "pamphlet epee arc". Cela fait doublon. Il y a 6 combinaisons possible pour chaque trio. 

Il va nous falloir changer, car, dans l'optique de faire un classement, nous devons enlever ce surplus. Sinon, les 6 premiers trio du classement seront la même combinaison des trois meilleurs objets. 

Pour cela, on va plutôt faire comme suit. 

``` python
print("A dev")
```


## Créer un Billy

Nous allons maintenant créer un Billy tout neuf. Premièrement, on ajoute les caractéristiques du Billy de base, celui qui n'est pas encore équipé. 

``` python
newBilly = [0, 0, 0, 0, 0, 0, 0, 0]
for j in range(len(newBilly)):
    newBilly[j] += BILLY_DEBUT[j]
```

Puis pour chaque objet, on ajoute ses caractéristiques.

``` python
# ajout des caracts liées aux objets
for i in objets:
    for j in range(len(newBilly)):
        newBilly[j] += caractObjet[i][0][j]
```

Ensuite on détermine la classe de notre Billy et on ajoute les caractéristiques correspondantes.

``` python
# détermine la classe de billy
classedeBilly = determ_billy_class(
    [caractObjet[objets[0]][1], caractObjet[objets[1]][1], caractObjet[objets[2]][1]])

# ajout des caracts liées a la classe
for j in range(len(newBilly)):
    newBilly[j] += caractClasse[classedeBilly][j]
```

Enfin, on ajoute les PV basé sur l'endurance de notre désormais accompli Billy.

``` python
# ajout des PV
newBilly[7] = 3 * newBilly[1]
```

Voilà !

## Les calculs

"Quels calculs faire ?", demanda le Pyro-Barbare, dont l'utilisation du mot "calcul" était aussi surprenante que le fait qu'il pose une question pareil. 

Pourtant, il va bien nous falloir faire des calculs pour déterminer le meilleur Billy. J'ai choisi trois outils statistiques courant que l'on va appliquer aux caractériques de chaque Billy : 
- la moyenne 
- la médiane
- la moyenne pondérée

### Moyenne pondérée ?

Il est à noté que chaque caractéristique ne vaut pas autant en terme de poids. Il y a des caractéristiques plus importantes que d'autres (comme l'habilité). Il faut donc poser une pondération sur ces stats. Disons : 
- habilité : 1
- endurance : 1
- adresse : 1
- chance : 1
- dégats : 1
- armure : 1
- critique : 1
- PV : 1

``` python
PONDERATION_CARACT = [1, 1, 1, 1, 1, 1, 1, 1]
```

1. La moyenne :
``` python
moy = 0
for j in range(len(billy)):
    moy += billy[j]
moy /= len(billy)
```

2. La médiane :
``` python
mediane = 0
buff = [0, 0, 0, 0, 0, 0, 0, 0]
for j in range(len(billy)):
    buff[j] += billy[j]

buff.sort()
if((len(buff) % 2) == 0):
    mediane = (buff[(int(len(buff)/2) - 1)] + buff[(int(len(buff)/2))]) / 2
else:
    mediane = buff[(int(len(buff)/2) - 1)]
```

3. La moyenne pondérée:
``` python
moyPond = 0
for j in range(len(billy)):
    moyPond += (billy[j] * PONDERATION_CARACT[j])

sommedesPond = 0
for i in PONDERATION_CARACT:
    sommedesPond += i
moyPond /= sommedesPond
```

## Un Billy au complet

``` python
# calcul de la moyenne
moyenne = calc_moyenne(newBilly)

# calcul de la médiane
mediane = calc_mediane(newBilly)

# calcul de la moyenne pondérée
moyennePond = calc_moyenne_ponderee(newBilly)
```

Nous pouvons maintenant créer un Billy au complet. On va lui donner ce format : 

```
format aBilly : [ [trio d'objets], [caractéristique], classe, moyenne, médiane, moyenne pondérée ]
```

Il ne nous reste plus qu'à trier les Billy selon une des trois caractéristiques finales. Par exemple : 

``` python
# sort la liste en fct des moyennes
print("Tri en fct des moyennes : ")
all_Billy = sorted(all_Billy, key=lambda l: l[3], reverse=True)
lesmeilleurs.append(all_Billy[0])
for i in range(0, maxAffichage):
    print_Billy(all_Billy[i])
print("\n")
```

On en profite pour ajouter le premier, donc le meilleur selon cet outil statistique, à une liste "lesmeilleurs". 

``` python
# les meilleurs
print("Les meilleurs Billy sont :\n")
for i in range (len(lesmeilleurs)):
    print("En fonction des", lesTris[i], ":")
    print_Billy(lesmeilleurs[i])
    print("")
```


## Le meilleur Billy

Nous voilà donc à la réponse. 

**LE**

**MEILLEUR**

**BILLY**

**EST**

**...**

... celui que vous choisirez, avec lequel vous prendrez plaisir à lire la magnifique histoire que nous offre Bob. N'hésitez pas à complimentez les cheveux de la centauresse, vous aurez la meilleur fin. 

Bon, mais d'un point de vue statistique ?

Eh bien, voyez par vous même. 

![image](https://user-images.githubusercontent.com/58084848/177020372-343ac28f-ce0d-4411-8eb2-45c4812e7b60.png)

Marmite, fourche et sac de grains feront de vous le meilleur Billy. 

Explication (à venir)




