s = "K1:L2"

def cellsInRange(s):
    route = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    coordinats = s.split(':')
    x1 = coordinats[0][0]
    y1 = int(coordinats[0][1])
    x2 = coordinats[1][0]
    y2 = int(coordinats[1][1])


    for x in alphabet[alphabet.index(x1):alphabet.index(x2)+1]:
        for y in range(y1,y2+1):
            route.append(x + str(y))

    return route






print(cellsInRange(s))