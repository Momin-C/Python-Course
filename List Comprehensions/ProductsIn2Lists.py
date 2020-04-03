lst1 = [2,4,6,8]
lst2 = [1,2,3,4]
result = []
"""
for i in lst1:
    if i in lst2:
        result.append(i)
print (result)
"""
result = [x for x in lst1 if x in lst2]
print (result)
