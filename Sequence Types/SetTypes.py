s = {5,3,1,100,1} #Does not allow duplicates
print (s)
print (type(s))

s.update([55,33,88,99]) # Inserts in random order
print (s)

s.remove(33)
print (s)

f = frozenset(s) #Freezes the set
print (type(f))
