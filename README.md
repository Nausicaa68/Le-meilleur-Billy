# Le-meilleur-Billy

Eh gamin ! Si tu t'es procuré *La Forteresse du chaudron Noir*, c'est certain, 

**TU**

**ES** 

**BILLY** 

**!!!**

Mais quel Billy es-tu ? Es-tu LE meilleur Billy ?

Moi, je suis un Billy informaticien. Et comme tout informaticien, j'informatise euh... j'automatise. Il y a 3 objets à choisir, parmi 12. Rend toi compte, gamin, cela fait 12×11×10 combinaisons possibles, soit 1320. En sachant que chaque objet donne des caractéristiques différentes, qu'une classe a des capacités spécifiques et que certaines caractéristiques de Billy sont plus importantes que d'autres, quelles sont les *3 objets* à choisir pour avoir le meilleuuuuuuuuuuuuuur Billy !?

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

Enfin, il est a noté que chaque stat ne vaut pas autant en terme de poids. Il y a des caractéristiques plus importantes que d'autres (comme l'habilité). Il faut donc poser une pondération sur ces stats. Disons : 
- habilité : 
- endurance : 
- adresse : 
- chance : 
- dégats : 
- armure : 
- critique : 
- PV : 

``` python
PONDERATION_CARACT = [1, 1, 1, 1, 1, 1, 1, 1]
```

## 1320 combinaisons, that a lot

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
 




