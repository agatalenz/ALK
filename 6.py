# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program realizujący iteracyjny algorytm generowania wszystkich podziałów zbioru {1, . . . , n}
# za pomocą przenoszenia między blokami elementu aktywnego.

# Przyznam się, że niezupełnie rozumiem ten algorytm :(

def findActiveElement(n, B, PR):

    j = n - 1

    if j == 1:
        return 1
    if (PR[j] and B[j] == j) or (PR[j] == False and B[j] == 1):
        return n

    return findActiveElement(n-1, B, PR)


def generateSubsetsDivs(n):

    B = [1] * n     # B[i] - numer bloku zawierającego element i
    N = [None] * n  # N[i] - numer następnego bloku dla bloku o numerze i
    P = [None] * n  # P[i] - numer poprzedniego bloku dla bloku o numerze i
    PR = [True] * n # tablica boolowska określająca kierunek poruszania się elementu aktywnego 
                    # (TRUE => PRAWO; FALSE => LEWO)
    j = n           # element aktywny

    # krok 1

    first = [x for x in range(1, n+1)]
    N[0] = 0

    print(first)
    P[n-1] = first

    while j != 1:

        # krok 2

        k = B[j-1]

        if PR[j-1]:

            # ii
            if N[k-1] == 0:
                N[k-1] = j
                N[j-1] = 0
                P[j-1] = k

            # iii
            elif N[k-1] > j:
                P[j-1] = k
                N[j-1] = N[k-1]
                P[N[j-1]-1] = j
                N[k-1] = j

            # i
            B[j-1] = N[k-1]
            

        else:

            # i
            B[j-1] = P[k-1]

            # ii
            if j == k and N[k-1] == 0:
                N[P[k-1]-1] = 0

            # iii
            elif N[k-1] != 0:
                N[P[k-1]-1] = N[k-1]
                P[N[k-1]-1] = P[k-1]

        PR[j-1] = False

        # krok 3

        j = findActiveElement(n, B, PR)
        print(B)


#generateSubsetsDivs(3)