import math

# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program generujący kod Prufera dla zadanego drzewa T o n wierzchołkach.


# znajdź największy wierzchołek stopnia 1

def getMaxNode(nodes):

    ranks = []

    for x in nodes:
        if x not in ranks and x > 0:
            ranks.append(x)

    x = 0

    for i in range(len(nodes)):
        if nodes[i] == min(ranks):
            x = i+1

    return x


# wygeneruj kod Prufera dla drzewa T

def generatePrufer(T):

    L = []
    d = [3, 1, 1, 2, 1, 2, 1, 3]
    n = len(d)

    while len(L) < n-2:

        x = getMaxNode(d)
        y = T[x][0]
        L.append(y)

        d[x-1] -= 1
        d[y-1] -= 1

        T[x].remove(y)
        T[y].remove(x)

    print(L)


Tree = {
    1: [7, 4, 6],
    2: [8],
    3: [8],
    4: [1, 5],
    5: [4],
    6: [1, 8],
    7: [1],
    8: [6, 2, 3]
}

# generatePrufer(Tree)


# --------------------------------------------------------------------------------------------
# Zadanie 2
# Napisz program wyznaczający drzewo odpowiadające zadanemu kodowi Prufera L.


# znajdź tablicę stopni wierzchołków

def getDegArr(L):

    d = []
    n = len(L)+2

    for x in range(1, n+1):
        d.append(L.count(x) + 1)

    return d


# odtwórz drzewo z kodu Prufera L

def getTree(L):

    n = len(L) + 2
    d = getDegArr(L)
    L.append(1)

    T = {}

    for x in range(n):
        T[x+1] = []

    while(d != [0] * n):

        x = getMaxNode(d)
        y = L.pop(0)

        d[x-1] -= 1
        d[y-1] -= 1

        T[x].append(y)
        T[y].append(x)

    for x, y in T.items():
        print(str(x) + " : " + str(y))


#getTree([1, 4, 1, 8, 8, 6])


# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program obliczający rangę kodu Prufera L.


def getRank(L):

    n = len(L) + 2
    L = [x-1 for x in L]
    r = 0

    i = len(L) - 1

    for x in L:
        r += x * n**i
        i -= 1

    print(r)


#getRank([1, 4, 1, 8, 8, 6])


# --------------------------------------------------------------------------------------------
# Zadanie 4
# Napisz program wyznaczający kod Prufera długości n−2 o randze r.


def generatePruferFromRank(r, n):

    L = {}

    for i in range(n-2, 0, -1):
        L[i] = r % n + 1
        r = math.floor((r-L[i]+1)/n)

    result = [key for key in L.values()]
    result.reverse()

    print(result)


#generatePruferFromRank(12797, 8)
