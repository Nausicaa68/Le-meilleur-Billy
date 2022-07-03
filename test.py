

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


count = 0
counter2 = 0
print(count)
print(counter2)
for key1 in caractObjet:
    for key2 in caractObjet:
        for key3 in caractObjet:
            if((key1 != key2) and (key1 != key3) and (key2 != key3)):
                count += 1
                #print(count, ":", key1, key2, key3)

                if(key1 == "epee" or key1 == "lance" or key1 == "arc"):
                    if(key2 == "epee" or key2 == "lance" or key2 == "arc"):
                        if(key3 == "epee" or key3 == "lance" or key3 == "arc"):
                            print(count, ":", key1, key2, key3)
                            counter2 += 1

print(count)
print(counter2)
