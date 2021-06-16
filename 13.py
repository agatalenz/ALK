# --------------------------------------------------------------------------------------------
# Zadanie 1
# Zaimplementuj algorytm Dijkstry znajdowania najkrótszych ścieżek z danego wierzchołka do wszystkich pozostałych wierzchołków w danym grafie z wagami na krawędziach.
# Można założyć, że wierzchołkiem źródłowym jest ten o numerze 1.
# Za wersję algorytmu z tablicą można dostać maksymalnie 0.7 punktu, a za wersję z kolejką priorytetową 1 punkt.
# Dla każdego wierzchołka grafu należy wypisać ścieżkę prowadzącą do niego ze źródła, o ile taka istnieje (w postaci ciągu kolejno odwiedzanych wierzchołków), oraz jej łączną wagę.

import sys
import pandas

# znajdź ścieżkę prowadzącą do wierzchołka v ze źródła source oraz jej łączną wagę


def getPath(p, v, source, G):

    nextVert = p[v]

    if nextVert == 0:
        return '-', 0

    cost = G[v][nextVert]

    if nextVert == source:
        return source + ' -> ' + v, cost

    else:
        path, c = getPath(p, nextVert, source, G)
        return path + ' -> ' + v, cost + c


# znajdź najkrótsze ścieżki z danego wierzchołka do wszystkich pozostałych wierzchołków w danym grafie z wagami

def Dijkstra(G, source):

    B = list(G.keys())
    d = {}
    p = {}

    for v in B:

        if v == source:
            d[v] = 0
        else:
            d[v] = sys.maxsize

        p[v] = 0

    while B:

        # szukamy w zbiorze 𝐵 wierzchołka 𝑘 o najniższej wartości 𝑑[𝑘]

        k = B[0]

        for v in B:
            if d[v] < d[k]:
                k = v

        # usuwamy go z B

        B.remove(k)

        # dla każdego sąsiada 𝑖 wierzchołka 𝑘 znajdującego się w zbiorze 𝐵 sprawdzamy, czy uda nam się dojść do niego szybciej przez wierzchołek 𝑘, czyli czy 𝑑[𝑘]+𝑤(𝑘,𝑖) < 𝑑[𝑖]
        # jeśli tak, to aktualizujemy 𝑑[𝑖] i ustawiamy 𝑝[𝑖]=𝑘.

        for v in G[k].items():

            i = v[0]
            w = v[1]

            cost = d[k] + w

            if cost < d[i]:
                d[i] = cost
                p[i] = k

    # dla każdego wierzchołka wyświetl ścieżkę prowadzącą do źródła oraz łączny koszt tej ścieżki

    paths = []
    costs = []

    for v in p.keys():
        path, cost = getPath(p, v, source, G)
        paths.append(path)
        costs.append(cost)

    d = {'wierzchołek v': list(p.keys()),
         'ścieżka do v': paths,
         'łączna waga ścieżki': costs}

    print(pandas.DataFrame(data=d).to_string(index=False))


# przeprowadź algorytm Dijkstry dla każdego wierzchołka grafu G

def RunDijkstra(G):

    for v in list(G.keys()):
        print('źródło: ' + v)
        print('-------------------------------------------------------')
        Dijkstra(G, v)
        print('-------------------------------------------------------\n')


# przykładowy graf

G = {
    '1': {'2': 3, '6': 10},
    '2': {'1': 3, '3': 8, '5': 1, '6': 10},
    '3': {'2': 8, '4': 6, '5': 3, '6': 2},
    '4': {'3': 6, '5': 1},
    '5': {'2': 1, '3': 3, '4': 1, '6': 4},
    '6': {'1': 10, '2': 10, '3': 2, '5': 4}
}

RunDijkstra(G)
