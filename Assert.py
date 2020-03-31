"""x=int(input("Enter a number >10: "))
assert x>10,"Wrong number entered!"
print ("You entered",x)"""
"""
x = int(input("Input a number: "))
for i in range (x):
    if i%10==0:
        continue
    if i>100:
        break
    print (i)
"""

x = int(input("Input a number: "))
for i in range (2,x):
    if x%i==0:
        primeFlag = False
        print ("Not a Prime No")
        break
    else:
        primeFlag = True
if primeFlag == True:
    print ("Prime No")
