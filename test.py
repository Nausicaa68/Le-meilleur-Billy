

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

allKeys = list(caractObjet.keys())
print(allKeys)

for i in range(0, len(allKeys)):
    for j in range(i+1, len(allKeys)):
        for k in range(j+1, len(allKeys)):
            # if((key1 != key2) and (key1 != key3) and (key2 != key3)):
            count += 1
            #print(count, ":", key1, key2, key3)
            print("i", i, "j", j, "k", k)
            print(count, ":", allKeys[i], allKeys[j], allKeys[k])

            if(allKeys[i] == "epee" or allKeys[i] == "lance" or allKeys[i] == "arc"):
                if(allKeys[j] == "epee" or allKeys[j] == "lance" or allKeys[j] == "arc"):
                    if(allKeys[k] == "epee" or allKeys[k] == "lance" or allKeys[k] == "arc"):
                        print("\t\t", count, ": ", allKeys[i], allKeys[j], allKeys[k])
                        counter2 += 1

print(count)
print(counter2)
