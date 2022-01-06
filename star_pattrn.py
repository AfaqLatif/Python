
n=int(input("Enter number for how much rows you want to print : "))
m=int(input("Enter 0 or 1 to print pattern : "))
x=bool(m)
if x==True:
    for i in range(0,n+1):
        for j in range(0,i):
            print("*",end=" ")
        print()
elif x==False:
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print()
else:
    print("Invalid input")