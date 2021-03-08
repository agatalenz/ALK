# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program generujący w porządku leksykograficznym wszystkie ciągi długości n 
# zbudowane z liczb od 1 do k (użyj algorytmu iteracyjnego).

def generateChains1(n, k):
    
    minValue = 1
    first = [minValue] * n

    current = first
    i = n - 1

    while not current == [k] * n:

        if current[i] < k:
            print(current)
            current[i] += 1
            current[i+1:] = [minValue] * (n - i - 1)
            i = n - 1       
        else:
            i -= 1
            if i < 0:
                i = n - 1

    print(current)

#generateChains1(4,3) 

# --------------------------------------------------------------------------------------------
# Zadanie 2
# Napisz program generujący wszystkie zbudowane z dodatnich liczb naturalnych ciągi długości n, 
# w których i-ty wyraz jest nie większy od i dla i = 1,2, . . . , n.

def generateChains2(n):

    minValue = 1
    first = [minValue] * n
    print(first)

    current = first
    i = n - 1

    while current[i] < i+1:

        current[i] += 1
        current[i+1:] = [minValue] * (n - i - 1)
        i = n - 1

        while current[i] == i+1 and i > 0:
            i -= 1
            if i < 0:
                i = n - 1
            
        print(current)

#generateChains2(4)

# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program generujący w porządku leksykograficznym wszystkie rosnące ciągi długości n 
# zbudowane z liczb od 1 do k (zakładamy, że k­>=n). 
# Pierwszy ciąg to (1,2, . . . , n), a ostatni to (k−n+ 1, . . . , k−1, k).

def generateChains3(n, k):  ### COŚ TU NIE DZIAŁA :((

    minValue = 1
    first = [x for x in range(minValue, n+1)] 
    print(first)

    current = first
    i = n - 1

    while current[i] < k - n + i + 1:
       
            current[i] += 1
            minValue = current[i] + 1
            current[i+1:] = [minValue] * (n - i - 1) 
            i = n - 1

            while current[i] == k - n + i + 1 and i > 0:
                    i -= 1
                    if i < 0:
                        i = n - 1   

            if i < n-1 and current[i] < current[i+1]:
                print(current)
            

#generateChains3(4, 5)

# --------------------------------------------------------------------------------------------
# Zadanie 4
# Napisz program generujący wszystkie podzbiory zbioru {1,2, . . . , n}, 
# wykorzystując bijekcję między ciągami binarnymi długości n a tymi podzbiorami.

def printChain(current, n):
    chain = []
    for i in range(n):
        if current[i] == 1:
            chain.append(i+1)
    print(chain)


def generateChains4(n):

    k = 2
    minValue = 1
    first = [minValue] * n

    current = first
    i = n - 1

    while not current == [k] * n:

        if current[i] < k:
            printChain(current, n)
            current[i] += 1
            current[i+1:] = [minValue] * (n - i - 1)
            i = n - 1       
        else:
            i -= 1
            if i < 0:
                i = n - 1

    printChain(current, n)

#generateChains4(4)