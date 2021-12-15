battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def validate_battlefield(field):
    shipped = []
    for i, row in enumerate(field):
        for col, item in enumerate(row):
            if item == 1:
                shipped.append((i, col))
    for tup in shipped:
        if 1 <= tup[0] <= 8 and 1 <= tup[1] <= 8:
            for corner in ((tup[0] - 1, tup[1] - 1),
                           (tup[0] - 1, tup[1] + 1),
                           (tup[0] + 1, tup[1] - 1),
                           (tup[0] + 1, tup[1] + 1)):
                if corner in shipped:
                    return False
            if (tup[0] - 1, tup[1]) in shipped:
                if (tup[0], tup[1] - 1) in shipped or\
                        (tup[0], tup[1] + 1) in shipped:
                    return False
            if (tup[0] + 1, tup[1]) in shipped:
                if (tup[0], tup[1] - 1) in shipped or\
                        (tup[0], tup[1] + 1) in shipped:
                    return False

    battleship = False
    cruisers_2 = False
    destroyers_3 = False
    submarines_4 = False
    while shipped:
        for tup in shipped:
            a, b, c = (tup[0] + 1, tup[1]), (tup[0] + 2,
                                             tup[1]), (tup[0] + 3, tup[1])
            if a in shipped:
                if b in shipped:
                    if c in shipped:
                        battleship += 1
                        shipped.remove(c)
                    else:
                        cruisers_2 += 1
                    shipped.remove(b)
                else:
                    destroyers_3 += 1
                shipped.remove(a)
                break
            a, b, c = (tup[0], tup[1] + 1), (tup[0],
                                             tup[1] + 2), (tup[0], tup[1] + 3)
            if a in shipped:
                if b in shipped:
                    if c in shipped:
                        battleship += 1
                        shipped.remove(c)
                    else:
                        cruisers_2 += 1
                    shipped.remove(b)
                else:
                    destroyers_3 += 1
                shipped.remove(a)
                break
            submarines_4 += 1
            shipped.remove(tup)
    print(battleship, cruisers_2, destroyers_3, submarines_4)
    return battleship == 1 and cruisers_2 == 2 and destroyers_3 == 3 and submarines_4 == 4


print(validate_battlefield(battleField))
