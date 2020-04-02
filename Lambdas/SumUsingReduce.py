from functools import reduce
lst = [5,10,15,20, "", 15, ""]
#reduce(lambda x,y:x+y,lst)
result = list(filter(None,lst))
print (result)
