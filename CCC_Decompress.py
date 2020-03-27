L = int(input("Input: "))
X = []
for counter in range (L):
    text = input()
    if text[1] == "0" or text[1] == "1" or text[1] == "2" or text[1] == "3" or text[1] == "4" or text[1] == "5" or text[1] == "6" or text[1] == "7" or text[1] == "8" or text[1] == "9":
        num = int(text[0:2])
        char = text[3]
    else:
        num = int(text[0])
        char = text[2]
    X.append(num*char)
for counter in range (L):
    print (X[counter])
