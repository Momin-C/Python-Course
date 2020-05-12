import logging
logging.basicConfig(filename="mylog.log",level=logging.DEBUG)

try:
    f = open("myfile.txt","w")
    a,b = [int(x) for x in input("Enter two numbers: ").split()]
    logging.info("Division in progress")
    c = a/b
    f.write("Writing %d into file"%c)
except ZeroDivisionError:
    print ("Division by zero is impossible")
    logging.error("ERROR! Division by Zero")
else:
    print("You have entered a non zero number")
finally:
    f.close()
    print("File Closed")
print ("Code after exception")
