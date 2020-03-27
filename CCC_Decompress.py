L = int(input("Input: "))
X = []
for counter in range (L):
<<<<<<< HEAD
    text = input("Num + Character: ")
=======
    text = input()
>>>>>>> f4a8faf82043d57c8c83d8d6767bc7f6ee63c491
    if text[1] != " ":
        num = int(text[0:2])
        char = text[3]
    else:
        num = int(text[0])
        char = text[2]
    X.append(num*char)
for counter in range (L):
    print (X[counter])


