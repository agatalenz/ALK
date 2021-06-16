# --------------------------------------------------------------------------------------------
# Zadanie 1
# Zaimplementuj algorytm Bellmana-Forda znajdowania najkrótszych ścieżek z danego wierzchołka
# do wszystkich pozostałych wierzchołków w danym grafie skierowanym z wagami na krawędziach.
# Można założyć, że wierzchołkiem źródłowym jest ten o numerze 1.
# Jeśli graf zawiera ujemny cykl, należy wypisać odpowiedni komunikat.
# W przeciwnym razie dla każdego wierzchołka grafu należy wypisać ścieżkę prowadzącą do niego ze źródła,
# o ile taka istnieje (w postaci ciągu kolejno odwiedzanych wierzchołków), oraz jej łączną wagę.

import sys
import pandas


# znajdź ścieżkę prowadzącą do wierzchołka v ze źródła source oraz jej łączną wagę

def getPath(p, v, source, G):

    prev = p[v]

    if prev == 0:
        if v == source:
            return '-', 0
        else:
            return 'x', 0

    else:

        cost = G[prev][v]

        if prev == source:
            return source + ' -> ' + v, cost

        path, c = getPath(p, prev, source, G)
        return path + ' -> ' + v, cost + c


# wykonaj relaksację dla podanej krawędzi e = (wierzchołek1, wierzchołek2, waga)

def EdgeRelaksation(e, d, p):

    v1 = e[0]
    v2 = e[1]
    w = e[2]

    if d[v1] + w < d[v2]:
        d[v2] = d[v1] + w
        p[v2] = v1


# wykonaj relaksację wszystkich krawędzi w grafie G

def Relaksation(G, d, p):

    for key in G.keys():
        for item in G[key].items():
            EdgeRelaksation((key, item[0], item[1]), d, p)


# przeprowadź algorytm Bellmana-Forda dla grafu G i określonego źródła source

def BellmanFord(source, G):

    B = list(G.keys())
    d = {}
    p = {}

    n = len(G.items())

    for v in B:
        if v == source:
            d[v] = 0
        else:
            d[v] = sys.maxsize

        p[v] = 0

    # wykonujemy relaksację wszystkich krawędzi n-1 razy

    for i in range(n-1):
        Relaksation(G, d, p)

    # dla każdego wierzchołka wyświetl ścieżkę prowadzącą do źródła oraz łączny koszt tej ścieżki

    paths = []
    costs = []

    for v in p.keys():
        path, cost = getPath(p, v, source, G)

        if path.__contains__('x'):
            cost = 0
            path = 'brak'

        paths.append(path)
        costs.append(cost)

    d = {'wierzchołek v': list(p.keys()),
         'ścieżka do v': paths,
         'łączna waga ścieżki': costs}

    print(pandas.DataFrame(data=d).to_string(index=False))


# przeprowadź algorytm Bellmana-Forda w celu znalezienia najkrótszych ścieżek z danego wierzchołka
# do wszystkich pozostałych wierzchołków w danym grafie skierowanym z wagami na krawędziach.

def RunBellmanFord(G):

    for v in list(G.keys()):
        print('źródło: ' + v)
        print('-------------------------------------------------------')
        BellmanFord(v, G)
        print('-------------------------------------------------------\n')


# przykładowy graf

G = {
    '1': {'2': 3, '6': 8},
    '2': {'3': 5, '5': 1, '6': 2},
    '3': {'4': -2, '5': 3, '6': -5},
    '4': {},
    '5': {'4': 1},
    '6': {'5': 4}
}

RunBellmanFord(G)
