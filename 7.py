# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz  program  generujący  funkcję  RGF f:{1, . . . , n} → Z+ odpowiadającą zadanemu podziałowi zbioru {1, . . . , n}.

def getRGF(n, B):

    k = len(B)
    f = [0] * n
    j = 1

    for i in range(k):

        while f[j-1] != 0:
            j += 1
        
        h = 1

        while len(B) > h and not(j in B[h-1]):
            h += 1

        for g in B[h-1]:
            f[g-1] = h

    print(f)


#getRGF(4, [ [1], [2,4], [3] ])


# --------------------------------------------------------------------------------------------
# Zadanie 2
# Napisz program generujący podział zbioru {1, . . . , n} odpowiadający zadanej funkcji RGF f:{1, . . . , n} → Z+.

def getSubsetDivs(f):

    n = len(f)
    k = 1

    for x in f:
        if x > k:
            k = x

    B = [[]] * k

    for j in range(1, n+1):
        B[f[j-1]-1].append(j)
        j += 1

    print(B)


#getSubsetDivs([1, 2, 3, 2])


# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program generujący wszystkie funkcje RGF f: {1, . . . , n} → Z+ w porządku leksykograficznym.

def generateRGF(n):

    f = [1] * n
    F = [2] * n
    stop = False

    while not stop:

        print(f)
        j = n

        while f[j-1] != F[j-1]:
            j -= 1

        if j > 0:

            f[j] += 1
            for i in range(j+1, n+1):
                f[i] = 1
                if f[j] == F[j]:
                    F[i] = F[j] + 1
                else:
                    F[i] = F[j]
        else:
            stop = True


#generateRGF(4)