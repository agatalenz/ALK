# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program obliczający pozycję podzbioru T ⊂ {1, . . . , n} w uporządkowaniu leksyko-graficznym
# (według wektorów charakterystycznych) podzbiorów zbioru {1, . . . , n}.

def getDecimal(binary):

    p = len(binary)
    decimal = 0

    for i in range(p):
        decimal += binary[i] * 2 ** (p-i-1)

    return decimal


def getRank(n, T):

    binary = []
    index = 0

    for i in range(n):      
        if T[index] == i+1:
            binary.append(1)
            index += 1
        else:
            binary.append(0)

    print(getDecimal(binary))


#getRank(5, [2,3,5])


# --------------------------------------------------------------------------------------------
# Zadanie 2
# Napisz program wyznaczający podzbiór T o zadanej pozycji r w uporządkowaniu leksyko-graficznym 
# według wektorów charakterystycznych) podzbiorów zbioru 1, . . . , n}.

def getBinary(n, decimal):

    binary = [0] * n

    for i in range(n):
        if decimal - 2 **  (n-i-1) >= 0:
            binary[i] = 1
            decimal -= 2 ** (n-i-1)

    return binary


def getSubset(n, rank):

    subset = []
    binary = getBinary(n, rank)

    for i in range(n):
        if binary[i] == 1:
            subset.append(i+1)

    print(subset)


#getSubset(5, 13)


# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program generujący w porządku leksykograficznym wszystkie ciągi długości n zbudowane z liczb od 1 do k. 
# Użyj algorytmu rekurencyjnego (nie używaj algorytmu następnika).

def generateChainsRecursively(n, k, current, pos):

    if pos == n:
        print(current)
    else:
        for i in range(k):
            current[pos] = i + 1
            generateChainsRecursively(n, k, current, pos+1)


def generateChains(n, k):

    first = [1] * n
    generateChainsRecursively(n, k, first, 0)


#generateChains(3,4)