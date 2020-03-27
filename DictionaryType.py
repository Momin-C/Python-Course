dict1= {1:"john",2:"bob",3:"bill"} # KEY: VALUE
print (dict1)
print (dict1.items())

k = dict1.keys() #Gives the first thing of the dictionary
for i in k: print (i)

v = dict1.values() #Gives the second thing
for i in v: print (i)

print (dict1[1]) #1 is the key

del dict1[2]
print (dict1)
