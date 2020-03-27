x = int(input())

x = str(x)

if x[0] != "-":
    x = x[::-1]
elif x[0] == "-":
    x = x[1:]
    x = x[::-1]
    x = "-" + x
print (x)
