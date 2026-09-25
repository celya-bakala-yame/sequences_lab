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
