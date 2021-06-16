# --------------------------------------------------------------------------------------------
# Zadanie 1
# Zaimplementuj algorytm Kruskala znajdowania minimalnego drzewa rozpinającego w danym grafie z wagami na krawędziach.
# Za wersję z listową reprezentacją zbiorów rozłącznych można dostać maksymalnie 0.7 punktu,
# za wersję z drzewiastą reprezentacją zbiorów rozłącznych maksymalnie 1 punkt.
# Program powinien wypisać listę krawędzi znalezionego drzewa oraz jego łączną wagę.


# znajdź wagę krawędzi e w grafie G
def GetRank(e, G):
    return G[e[0]][e[1]]


# znajdź listę krawędzi w grafie G
def GetEdges(G):

    E = []

    for key in G.keys():
        for destination, cost in G[key].items():
            x = (key, destination)

            if not E.__contains__((destination, key)):
                E.append(x)

    return E


# posortuj krawędzie grafu G w porządku niemalejących wag
def GetSortedEdges(G):

    Edges = GetEdges(G)
    E = []
    ranks = []

    for e in Edges:
        rank = GetRank(e, G)
        if not ranks.__contains__(rank):
            ranks.append(rank)

    ranks.sort()

    for rank in ranks:
        for e in Edges:
            if GetRank(e, G) == rank:
                E.append(e)

    return E


# sprawdź, czy istnieje ścieżka łącząca wierzchołki w1 i w2 w zbiorze krawędzi E
def CheckPath(w1, w2, E):

    if E == []:
        return False

    destinations = []
    ECopy = []

    for edge in E:
        if edge[0] == w1:
            destinations.append(edge[1])
        elif edge[1] == w1:
            destinations.append(edge[0])
        else:
            ECopy.append(edge)

    if destinations.__contains__(w2):
        return True

    else:
        for w in destinations:
            if CheckPath(w, w2, ECopy):
                return True

    return False


# sprawdź, czy dodanie krawędzi e do danego zbioru krawędzi E nie spowoduje powstania cyklu
def CheckForCycle(e, E):
    return CheckPath(e[0], e[1], E)


# znajdź minimalne drzewo rozpinające dla grafu G
def MSTKruskal(G):

    E = GetSortedEdges(G)
    n = len(G) - 1
    T = []
    rankSum = 0

    for e in E:
        if n > 0 and not CheckForCycle(e, T):
            T.append(e)
            rankSum += GetRank(e, G)
            n -= 1

    print("Zbiór krawędzi: ", T)
    print("Suma wag: ", rankSum)


G = {
    '1': {'2': 1, '3': 2},
    '2': {'1': 1, '3': 2, '4': 3, '5': 5},
    '3': {'1': 2, '2': 2, '4': 3, '6': 3},
    '4': {'2': 3, '3': 3, '5': 1, '6': 4},
    '5': {'2': 5, '4': 1, '6': 3, '7': 1},
    '6': {'3': 3, '4': 4, '5': 3, '7': 4},
    '7': {'5': 1, '6': 4}
}

MSTKruskal(G)
