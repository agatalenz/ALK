import scipy.special

# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program wyznaczający następnik k-elementowego podzbioru T zbioru {1, . . . , n}
# w uporządkowaniu leksykograficznym podzbiorów k-elementowych.

# OK

# znajdź pozycję, na której element nie ma wartości maksymalnej (jeśli taka istnieje)

def checkMax(chain, maxVals, pos):

    if pos == -1 or chain[pos] != maxVals[pos]:
        return pos
    else:
        return checkMax(chain, maxVals, pos-1)

# znjdź następnik podzbioru T zbioru {1, . . . , n}

def getNext(n, T):

    k = len(T)
    maxVals = [x for x in range(k+1, n+1)]
    pos = checkMax(T, maxVals, k-1)
    
    if pos == -1:
        print("brak następnika")

    else:
        T[pos] += 1
        for i in range(pos+1, k):
            T[i] = T[i-1] + 1

        print(T)


#getNext(8, [1, 2, 7, 8])


# --------------------------------------------------------------------------------------------
# Zadanie 2
# Napisz program obliczający rangę k-elementowego podzbioru T zbioru {1, . . . , n}
# w uporządkowaniu leksykograficznym podzbiorów k-elementowych.

# OK

def getRank(n, T):

    r = 0
    k = len(T)
    T.insert(0,0)

    for i in range (1, k+1):
        if T[i-1] + 1 <= T[i] - 1:
            for j in range(T[i-1]+1, T[i]):
                r += scipy.special.binom(n-j, k-i)

    print(int(r))


#getRank(5, [2, 3, 5])


# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program wyznaczający podzbiór T o randze r w uporządkowaniu leksykograficznym
# k-elementowych podzbiorów zbioru {1, . . . , n}.

# OK

def getSubset(n, k, r):

    x = 1
    T = [0] * k

    for i in range(1, k+1):
        
        binom = int(scipy.special.binom(n-x, k-i))
        while binom <= r:
            r -= binom
            x += 1
            binom = int(scipy.special.binom(n-x, k-i))
        
        T[i-1] = x
        x += 1

    print(T)

#getSubset(5, 3, 7)