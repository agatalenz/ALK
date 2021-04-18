# Algorytmy kombinatoryczne

# [1.py](https://git.wmi.amu.edu.pl/s444426/ALK/src/branch/master/1.py) Ciągi

1. Napisz program generujący w porządku leksykograficznym wszystkie ciągi długości n zbudowane z liczb od 1 do k (użyj algorytmu iteracyjnego).
2. Napisz program generujący wszystkie zbudowane z dodatnich liczb naturalnych ciągi długości n, w których i-ty wyraz jest nie większy od i dla i = 1,2, . . . , n.
3. Napisz program generujący w porządku leksykograficznym wszystkie rosnące ciągi długości n zbudowane z liczb od 1 do k (zakładamy, że k­>=n). Pierwszy ciąg to (1,2, . . . , n), a ostatni to (k−n+ 1, . . . , k−1, k).
4. Napisz program generujący wszystkie podzbiory zbioru {1,2, . . . , n wykorzystując bijekcję między ciągami binarnymi długości n a tymi podzbiorami.

# [2.py](https://git.wmi.amu.edu.pl/s444426/ALK/src/branch/master/2.py) Podzbiory

1. Napisz program obliczający pozycję podzbioru T ⊂ {1, . . . , n} w uporządkowaniu leksyko-graficznym (według wektorów charakterystycznych) podzbiorów zbioru {1, . . . , n}.
2. Napisz program wyznaczający podzbiór T o zadanej pozycji r w uporządkowaniu leksyko-graficznym według wektorów charakterystycznych) podzbiorów zbioru 1, . . . , n}.
3. Napisz program generujący w porządku leksykograficznym wszystkie ciągi długości n zbudowane z liczb od 1 do k. Użyj algorytmu rekurencyjnego (nie używaj algorytmu następnika).

# [3.py](https://git.wmi.amu.edu.pl/s444426/ALK/src/branch/master/3.py) Kod Graya

1. Napisz program generujący wszystkie podzbiory zbioru {1, . . . , n} w porządku minimalnych zmian (Graya), wykorzystując wagi Hamminga lub różnicę symetryczną zbiorów.
2. Napisz program obliczający rangę podzbioru T⊂{1, . . . , n} w uporządkowaniu minimalnych zmian (Graya) podzbiorów zbioru {1, . . . , n}.
3. Napisz program wyznaczający podzbiór T o zadanej pozycji r w uporządkowaniu minimalnych zmian (Graya) podzbiorów zbioru {1, . . . , n}.

# [4.py](https://git.wmi.amu.edu.pl/s444426/ALK/src/branch/master/4.py) Podzbiory k-elementowe

1. Napisz program wyznaczający następnik k-elementowego podzbioru T zbioru {1, . . . , n} w uporządkowaniu leksykograficznym podzbiorów k-elementowych.
2. Napisz program obliczający rangę k-elementowego podzbioru T zbioru {1, . . . , n} w uporządkowaniu leksykograficznym podzbiorów k-elementowych.
3. Napisz program wyznaczający podzbiór T o randze r w uporządkowaniu leksykograficznym k-elementowych podzbiorów zbioru {1, . . . , n}.

# [5.py](https://git.wmi.amu.edu.pl/s444426/ALK/src/branch/master/5.py) Liczby Stirlinga

1. Napisz program obliczający za pomocą programowania dynamicznego wartości liczb Stirlinga drugiego rodzaju ze wzoru: S(n, k) = kS(n−1, k) + S(n−1, k−1), gdzie S(n, n+1) = 0 dla n­>=0, S(n,0) = 0 dla n>=­1 i S(0,0) = 1.
2. Napisz program obliczający za pomocą programowania dynamicznego wartości liczb Stirlingapierwszego rodzaju ze wzoru:s(n, k) = s(n−1, k−1) − (n−1)s(n−1, k), gdzie s(n, n+ 1) = 0 dla n>=­0 , s(n,0) = 0 dla n>=­1 i s(0,0) = 1.
3. Napisz program obliczający za pomocą programowania dynamicznego wartości liczb Bella.

# [6.py](https://git.wmi.amu.edu.pl/s444426/ALK/src/branch/master/6.py) Generowanie podziałów zbioru

1. Napisz program realizujący iteracyjny algorytm generowania wszystkich podziałów zbioru {1, . . . , n} za pomocą przenoszenia między blokami elementu aktywnego.
