#Global Keyword
"""x=15
def func(n):
    print(n)
    global x
    x=12
    y=15
    print("Value of x : ",x," And value of y : ",y)

func("Function called")
print("Value of x outside function : ",x)


#Factorial by using iterations
def fact_itrative(nmbr):
    fact=1
    for i in range(nmbr):
        fact=fact*(i+1)
    return fact

#print("Enter no. to calculate factorial")
n=int(input("Enter no. to calculate factorial : "))
factorial=fact_itrative(n)
print("Factorial of given number is ",factorial)



#Factorial by using recursion
def fact_recursive(nmbr):
    if nmbr==1:
        return 1
    else:
        return nmbr*fact_recursive(nmbr-1)

print("Enter no. to calculate factorial")
n=int(input())
factorial=fact_recursive(n)
print("Factorial of given number is ",factorial)
"""



#Fibonache series
def fibo_series(nmbr):
    x=int(input("Enter no. 1 "))
    y=int(input("Enter no. 2 "))
    print(x)
    print(y)
    for i in range(nmbr):
        z=x+y
        print(z)
        x=y
        y=z
    return 0

n=int(input("Enter no. to print fibonachi_series "))
fibo_series(n)