from functools import reduce
lst = [5,10,15,20]
#reduce(lambda x,y:x+y,lst)
result = reduce(lambda x,y:x+y,lst)
print (result)
