# Zadanie 1
# Napisz program generujący w porządku leksykograficznym wszystkie ciągi długościnzbu-dowane z liczb od 1 do k (użyj algorytmu iteracyjnego).

def generateChain(n, k):
    
    current = [1] * n
    x = n - 1

    print(current)

    while not current == [k] * n:

        if current[x] < k:
            current[x] += 1
            current[x+1:] = [1] * (n - x - 1)
            x = n - 1
        else:
            x -= 1
            if x < 0:
                x = n - 1

        print(current)


# Zadanie 2
# Napisz program generujący wszystkie zbudowane z dodatnich liczb naturalnych ciągi długości n, 
# w których i-ty wyraz jest nie większy od i dla i = 1,2, . . . , n.

# Zadanie 3
# Napisz program generujący w porządku leksykograficznym wszystkie rosnące ciągi długości n zbudowane z liczb od 1 do k (zakładamy, że k­>=n). 
# Pierwszy ciąg to (1,2, . . . , n), a ostatni to (k−n+ 1, . . . , k−1, k).

# Zadanie 4
# Napisz program generujący wszystkie podzbiory zbioru {1,2, . . . , n}, wykorzystując bijekcję między ciągami binarnymi długości n a tymi podzbiorami.


    
# generateChain(4,3)