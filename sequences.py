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

print(l)

print(l.__contains__(0)) #dispose bien des memes méthodes que les séquences de type str, list, tuple, etc.
print(l.__contains__(10))

#mais elle dispose de plus de méthode, permettant de mofidier la liste tel que :

l.append(5)
print(l)

l.remove(0)
print(l)

l.insert(0, 0)
print(l)
