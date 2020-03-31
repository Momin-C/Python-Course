def calculator(a,b): #Could also be (a=10,b=20) which would be default param
    sum = a+b
    difference = abs(a-b)
    product = a*b
    quotient = a/b
    average = (a+b)/2
    return (sum,difference,product,quotient,average)
print (calculator(5,10))
