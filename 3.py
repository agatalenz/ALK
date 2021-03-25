# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program generujący wszystkie podzbiory zbioru {1, . . . , n} 
# w porządku minimalnych zmian (Graya), 
# wykorzystując wagi Hamminga lub różnicę symetryczną zbiorów.

# brakuje ostatniego zbioru

# zamień bit na wskazanej pozycji
def switchBit(binary, index):
    
    if binary[index] == 1:
        binary[index] = 0
    else:
        binary[index] = 1
    
# zamień ciąg binarny na odpowiadający mu podzbiór zbioru {1, . . . , n}
def binaryToSubset(binary):

    n = len(binary)
    subset = []

    for i in range(n):
        if binary[i] == 1:
            subset.append(i+1)

    return subset

# znajdź następnika  wskazanego ciągu binarnego w porządku Graya
def getNext(current):

    _next = current.copy()

    if _next.count(1) % 2 == 0:
        switchBit(_next, -1)
    else:
        index = len(_next) - 1 - _next[::-1].index(1)
        if index > 0:
            switchBit(_next, index-1)

    return _next

# wygeneruj wszystkie podzbiory zbioru {1, . . . , n} w porządku Graya
def generateSubsets(n):

    current = [0] * n
    _next = getNext(current)

    while(current != _next):

        print(binaryToSubset(current))
        current = _next
        _next = getNext(_next)


#generateSubsets(4)


# --------------------------------------------------------------------------------------------
# Zadanie 2
# Napisz program obliczający rangę podzbioru T⊂{1, . . . , n} 
# w uporządkowaniu minimalnych zmian (Graya) podzbiorów zbioru {1, . . . , n}.

# OK

# zamień podzbiór zbioru {1, . . . , n} na odpowiadający mu ciąg binarny
def subsetToBinary(subset, n):

    binary = [0] * n
    for i in range(n):
        if subset.count(i+1) == 1:
            binary[i] = 1
        else:
            binary[i] = 0
    return binary

# zamień ciąg binarny na wartość dziesiętną
def getDecimal(binary):

    p = len(binary)
    decimal = 0

    for i in range(p):
        decimal += binary[i] * 2 ** (p-i-1)

    return decimal

# oblicz rangę podzbioru T⊂{1, . . . , n} w uporządkowaniu Graya
def getRank(T, n):

    binRank = []
    prevBit = 0
    binary = subsetToBinary(T, n)

    for i in range(n):
        binRank.append(binary[i] ^ prevBit)
        prevBit = binRank[i]

    print(getDecimal(binRank))
    

#getRank([1,3], 4)


# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program wyznaczający podzbiór T o zadanej pozycji r 
# w uporządkowaniu minimalnych zmian (Graya) podzbiorów zbioru {1, . . . , n}.

# OK

# zamień liczbę dziesiętną na ciąg binarny o zadanej długości
def getBinary(decimal, n):

    binary = [0] * n

    for i in range(n):
        if decimal - 2 **  (n-i-1) >= 0:
            binary[i] = 1
            decimal -= 2 ** (n-i-1)

    return binary

# znajdź podzbiór zbioru {1, . . . , n} o zadanej randze w uporządkowaniu Graya
def getSubset(rank, n):

    binRank = getBinary(rank, n)
    divRank = getBinary(rank/2, n)
    xorRank = [b1 ^ b2 for b1, b2 in zip(binRank, divRank)]

    print(binaryToSubset(xorRank))


#getSubset(12, 4)