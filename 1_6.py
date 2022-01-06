def math_func(n1,n2):
    
    sum=n1+n2
    print("Sum of numbers :",sum)
    sub=n1-n2
    print("Sub of numbers :",sub)
    mul=n1*n2
    print("Mul of numbers :",mul)
    div=n1/n2
    print("Div of numbers :",div)

    return 0

def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    math_func(a,b)

if __name__ == "__main__":
    main()
