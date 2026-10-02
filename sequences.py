import sys
import timeit
from array import array
from bisect import bisect_left, insort
from collections import deque


def echiquier():
    """
    >>> cases = echiquier()
    >>> len(cases), len(cases[0])
    (8, 8)
    >>> cases[0]
    ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
    >>> cases[-1][-1]
    'H8'
    """
    return [
        ["".join((chr(i), str(j))) for i in range(65, 73)]
        for j in range(1, 9)
    ]


def gen(i):
    """
    >>> list(gen(5))
    [0, 1, 2, 3, 4]
    >>> list(gen(0))
    []
    >>> g = gen(2)
    >>> next(g)
    0
    >>> next(g)
    1
    >>> list(g)
    []
    """
    for j in range(i):
        yield j


def inserer_trie(nombres, valeur):
    """
    >>> nombres = [1, 3, 5]
    >>> inserer_trie(nombres, 4)
    [1, 3, 4, 5]
    >>> nombres
    [1, 3, 5]
    >>> inserer_trie([], 2)
    [2]
    >>> inserer_trie([1, 3, 3], 3)
    [1, 3, 3, 3]
    """
    copie = nombres.copy()
    insort(copie, valeur)
    return copie


if __name__ == "__main__":
    s = "abc"
    l = list(range(5))

    print(s.__len__(), len(s))
    print(s.__contains__("a"), "a" in s)
    print(s.__getitem__(0), s[0])
    print(s.index("b"), s.count("b"))

    i = iter(s)
    print(next(i), next(i), next(i))

    for c in s:
        print(c)

    print(l)
    print(0 in l)
    print(10 in l)

    l.append(5)
    print(l)

    l.remove(0)
    print(l)

    l.insert(0, 0)
    print(l)

    l.extend(range(6, 10))
    print(l)

    print(l.pop())
    print(l)

    l = [ord(i) for i in "abcde"]
    print(l)

    l = [chr(i) for i in range(73, 83) if i % 2 == 0]
    print(l)

    l = [
        chr(i) if chr(i).isalpha() else "NA"
        for i in range(89, 99)
    ]
    print(l)

    l = echiquier()
    print(l)

    print(timeit.timeit("[i for i in range(10**6)]", number=10))

    g = gen(10**6)
    print(g)
    print(next(g))
    print(next(g))

    for valeur in gen(5):
        print(valeur)

    l = [i for i in range(10**6)]
    print("Taille de la liste en octets :", sys.getsizeof(l))
    print("Taille du générateur en octets :", sys.getsizeof(g))

    nombres = [0, 1, 2, 3, 4, 5]

    print(nombres[1:4])
    print(nombres[::2])
    print(nombres[::-1])
    print(nombres[-1])

    nombres = [3, 1, 2]

    nouvelle_liste = sorted(nombres)
    print(nouvelle_liste)
    print(nombres)

    resultat = nombres.sort()
    print(nombres)
    print(resultat)

    print(sorted(nombres, reverse=True))

    mots = ["python", "chat", "a"]
    print(sorted(mots, key=len))

    nombres = [1, 3, 5, 7]

    position = bisect_left(nombres, 4)
    print(position)

    insort(nombres, 4)
    print(nombres)

    print(inserer_trie(nombres, 6))
    print(nombres)

    file = deque(["Alice", "Bob"])
    file.append("Célya")
    print(file.popleft())

    file.appendleft("Zoé")
    print(list(file))
    print(file.pop())

    entiers = array("i", [1, 2, 3])
    entiers.append(4)

    print(entiers.tolist())
    print(entiers.typecode)
    print(entiers.itemsize)