# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program generujący wszystkie podzbiory zbioru {1, . . . , n} 
# w porządku minimalnych zmian (Graya), 
# wykorzystując wagi Hamminga lub różnicę symetryczną zbiorów.

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



# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program wyznaczający podzbiór T o zadanej pozycji r 
# w uporządkowaniu minimalnych zmian (Graya) podzbiorów zbioru {1, . . . , n}.