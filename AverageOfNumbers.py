"""a,b,c = [int(x) for x in input("Enter three integers: ").split()]
average = (a+b+c)/3
print (average)"""
"""
a,b,c = [int(x) for x in input("Enter marks for Math Physics Chemistry seperated by a space: ").split()]

if a >=35 and b>=35 and c>=35:
    average = (a+b+c)/3
    if average<= 59:
        print ("Grade: C")
    elif average<=69 and average>59:
        print ("Grade: B")
    elif average>69:
        print ("Grade: A")
else:
    print ("You have failed the exam")
"""
"""
x = int(input("Min: "))
y = int(input("Max: "))
if x%2 ==0:
    x+=1
while x<=y:
    print (x)
    x+=2
"""
x=int(input("Enter Number: "))
for i in range (1,11):
    print (x*i)
