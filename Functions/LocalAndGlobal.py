x = 123
def display():
    x = 678 #This is a local variable
    print ("Local:",x) #This is a global variable
    print ("Global:",globals()['x'])
display()

z = display
z()
