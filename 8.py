import numpy as np

# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program generujący następnik permutacji p zbioru {1, . . . , n} w porządku leksykograficznym.

# OK


def getNext(p):

    n = len(p)
    i = n-2

    # szukamy indeksu i

    while i >= 0 and p[i] >= p[i+1]:
        i -= 1

    if(i == -1):
        print("Następnika nie ma.")

    else:

        p_i = p[i]
        j = n-1

        # szukamy indeksu j

        while j >= 0 and p[j] <= p[i]:
            j -= 1

        # zamiana miejscami p[i] z p[j]

        p[i] = p[j]
        p[j] = p_i

        next_p = p.copy()

        # odwrócenie podciągu p[i+1, ..., n]

        cnt = -1

        for idx in range(i+1, n):
            next_p[idx] = p[cnt]
            cnt -= 1

        print(next_p)


#getNext([3, 6, 2, 7, 5, 4, 1])
#getNext([7, 6, 5, 4, 3, 2, 1])


# --------------------------------------------------------------------------------------------
# Zadanie 2
# Napisz program obliczający rangę permutacji p zbioru {1, . . . , n} w porządku leksykograficznym.

# OK

def silnia(n):

    if n == 0 or n == 1:
        return 1

    else:
        return n * silnia(n-1)


def getRank(p):

    n = len(p)
    r = 0

    for j in range(0, n):

        r = r + (p[j] - 1) * silnia(n-j-1)

        for i in range(j+1, n):
            if p[i] > p[j]:
                p[i] -= 1

    print(r)


#getRank([2, 4, 1, 3])


# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program wyznaczający permutację p zbioru {1, . . . , n} o randze r w porządku leksykograficznym.

# OK

def getPerm(n, r):

    p = [None] * n
    p[n-1] = 1

    for j in range(0, n-1):

        d = (r % silnia(j+2)) / silnia(j+1)
        r -= d * silnia(j+1)
        p[n-j-2] = d+1

        for i in range(n-j-1, n):
            if(p[i] > d):
                p[i] += 1

    print(list(map(int, p)))


#getPerm(4, 10)
