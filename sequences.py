import timeit
import sys
from bisect import bisect_left, insort
from collections import deque
from array import array

s = "abc"
l = list(range(5))

#i = s.__iter__()

#for c in s : 
#    print(c)

##print(s.__len__(), ",", len(s))
#print(s.__contains__('a'), ",", 'a' in s)

#print(i.__next__(), i.__next__(), i.__next__())

#print(s.__getitem__(0), ",", s[0])

#print(s.index('b'), ",", s.count('b'))

#print(l)

#print(l.__contains__(0)) #dispose bien des memes méthodes que les séquences de type str, list, tuple, etc.
#print(l.__contains__(10))

#mais elle dispose de plus de méthode, permettant de mofidier la liste tel que :

#l.append(5)
#print(l)

#l.remove(0)
#print(l)

#l.insert(0, 0)
#print(l)

#l.extend(list(range(5, 10)))
#print(l)

#l.pop()

l = [ ord(i) for i in 'abcde' ]
print(l)

l = [ chr(i) for i in range(73,83) if i%2==0 ]
print(l)

l = [ chr(i) if chr(i).isalpha() else 'NA' for i in range(89,99) ]
print(l)

l = [ [ "".join((chr(i),str(j))) for i in range(65,73) ] for j in range(1,9) ]
print(l)

print(timeit.timeit('[i for i in range(int(1e6))]', number=10))

def gen(i):
    for j in range(i):
        yield j
        
g = gen(int(1e6))

#for i in g: print(i)

print(g)
print(next(g))
print(next(g))

#l = [i for i in range(int(1e6)) ]
print(l)
print("Taille de la liste en octets :", sys.getsizeof(l))

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