# --------------------------------------------------------------------------------------------
# Zadanie 1
# Zaimplementuj algorytm Prima znajdowania minimalnego drzewa rozpinającego w danym grafie z wagami na krawędziach.
# Za wersję naiwną (z tablicą) można dostać maksymalnie 0.7 punktu, za wersję z kolejką priorytetową maksymalnie 1 punkt.
# Program powinien wypisaćlistę krawędzi znalezionego drzewa oraz jego łączną wagę.

# Wersja z tablicą. Łączna waga drzewa nie jest wypisana (0.65 pkt).

def MST(E, start):

    n = 0
    for x in E.items():
        n += 1

    S = [start]
    Q = []
    G = []

    for destination, cost in E[start].items():
        x = [start, destination, cost]
        Q.append(x)

    while len(S) != n:

        for elem in Q:
            if elem[0] in S and elem[1] in S:
                Q.remove(elem)

        temp = Q[0][2]
        best = Q[0]

        for q in Q:
            if q[2] < temp:
                best = q
                temp = q[2]

        edge = best

        Q.remove(edge)
        start = edge[1]

        S.append(start)
        G.append(edge)

        e0 = edge[0]
        e1 = edge[1]

        E[e0].pop(e1)
        E[e1].pop(e0)

        for destination, cost in E[start].items():
            x = [start, destination, cost]
            Q.append(x)

        for elem in Q:
            if elem[0] in S and elem[1] in S:
                Q.remove(elem)

    for x in G:
        print(x)


E = {
    '1': {'2': 1, '3': 4},
    '2': {'1': 1, '3': 2, '4': 3, '5': 5},
    '3': {'1': 4, '2': 2, '4': 3, '6': 2},
    '4': {'2': 3, '3': 3, '5': 1, '6': 4},
    '5': {'2': 5, '4': 1, '6': 3, '7': 5},
    '6': {'3': 2, '4': 4, '5': 3, '7': 4},
    '7': {'5': 5, '6': 4}
}


MST(E, '1')
