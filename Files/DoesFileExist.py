import os,sys
if os.path.isfile("myfile.txt"):
    f = open("myfile.txt","r")
else:
    print ("NO! IT DOES NOT EXIST!")
    sys.exit()
print(f.read())
