import numpy as np

# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program obliczający metodą programowania dynamicznego liczbę podziałów liczby n na k składników,
# korzystając ze wzoru: P(n, k) = P(n−1, k−1) + P(n−k, k) dla k<=n, gdzie P(0,0) = 1 oraz P(i,0) = 0 dla i > 0.

# OK


def getDivsNumber(n, k):

    P = np.zeros((n+1, k+1), int)
    P[0][0] = 1

    for i in range(n+1):
        for j in range(1, k+1):
            P[i][j] = P[i-1][j-1] + P[i-j][j]

    print(P[n][k])


#getDivsNumber(10, 2)


# --------------------------------------------------------------------------------------------
# Zadanie 2
# Napisz program generujący podział sprzężony do zadanego podziału (a1, . . . , am) liczby n.

# OK

def getConjugateDiv(div):

    conjugate = [1] * div[0]

    for i in range(1, len(div)):
        ii = div[i]

        for j in range(ii):
            conjugate[j] += 1

    print(conjugate)


#getConjugateDiv([4, 3, 2, 2, 1])


# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program generujący wszystkie podziały liczby n w postaci normalnej za pomocą algorytmu rekurencyjnego.
# Wykorzystaj następującą procedurę:
#
# PODZIAŁ (n, b, m)
#   if n == 0 then wypisz (a1, . . . , am)
#   else
#       for i = 1 to min(b, n)
#       do
#           a(m + 1) = i
#           PODZIAŁ (n−i, i, m + 1)
#
# W powyższym pseudokodzie a1, . . . , am są już wybranymi składnikami podziału,
# natomiast parametr b jest górnym ograniczeniem wartości następnego generowanego składnika.

# OK

def generateDivsRecursively(a, n, b, m):

    if n == 0:
        print(list(filter(None, a[:m+1])))
    else:
        for i in range(1, min(b, n) + 1):
            a[m+1] = i
            generateDivsRecursively(a, n-i, i, m+1)


def generateDivs(n):

    a = [None] * (n+1)
    generateDivsRecursively(a, n, n, 0)


# generateDivs(5)


# --------------------------------------------------------------------------------------------
# Zadanie 4
# Napisz program generujący wszystkie podziały liczby n na k składników.
# Wykorzystaj algorytmy z zadań 2 i 3.

# OK

def generateDivsRecursively2(a, n, b, m):

    if n == 0:
        getConjugateDiv(list(filter(None, a[:m+1])))

    else:
        for i in range(1, min(b, n) + 1):
            a[m+1] = i
            generateDivsRecursively2(a, n-i, i, m+1)


def generateDivs2(n, k):

    a = [None] * (n+1)
    a[0] = k
    generateDivsRecursively2(a, n-k, k, 1)


#generateDivs2(10, 5)
