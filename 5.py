import scipy.special

# --------------------------------------------------------------------------------------------
# Zadanie 1
# Napisz program obliczający za pomocą programowania dynamicznego wartości liczb Stirlinga drugiego rodzaju ze wzoru: 
# S(n, k) = kS(n−1, k) + S(n−1, k−1), 
# gdzie S(n, n+1) = 0 dla n­>=0, S(n,0) = 0 dla n>=­1 i S(0,0) = 1.

def appendNumber(S, i, j, n, stirlingType):

    if j == 0 and i == 0:
        S[i].append(1)

    elif j == 0 and n > 0:
        S[i].append(0)

    elif j == i and j > 0:
        S[i].append(1)

    elif j <= i:
        if stirlingType == 1:
            nextNum = S[i-1][j-1] - (i-1) * S[i-1][j]
        else:
            nextNum = j * S[i - 1][j] + S[i - 1][j - 1]     
        S[i].append(nextNum)


def getStirling2(n, k):
    
    if k > n:
        print("Nie ma takiej liczby")
    
    else:

        S = [[]] * n
        for i in range(n):
            for j in range(k):
                appendNumber(S, i, j, n, 2)

        print(S[n-1][k-1])


#getStirling2(5, 1)


# --------------------------------------------------------------------------------------------
# Zadanie 2
# Napisz program obliczający za pomocą programowania dynamicznego wartości liczb Stirlinga
# pierwszego rodzaju ze wzoru:
# s(n, k) = s(n−1, k−1) − (n−1)s(n−1, k), 
# gdzie s(n, n+ 1) = 0 dla n>=­0 , s(n,0) = 0 dla n>=­1 i s(0,0) = 1.

def getStirling1(n, k):

    if k > n:
        print("Nie ma takiej liczby")
    
    else:

        S = [[]] * n
        for i in range(n):
            for j in range(k):
                appendNumber(S, i, j, n, 1)

        print(S[n-1][k-1])


#getStirling1(5, 2)


# --------------------------------------------------------------------------------------------
# Zadanie 3
# Napisz program obliczający za pomocą programowania dynamicznego wartości liczb Bella.

def getBellNumber(n):

    B = [1]

    for i in range(1, n+1):
        num = 0
        for k in range(i):
            num += scipy.special.binom(i - 1, k) * B[k]
        B.append(num)

    print(B[n])


#getBellNumber(5)