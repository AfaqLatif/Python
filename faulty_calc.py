print("Enter + for addition")
print("Enter - for subtruction")
print("Enter / for division")
print("Enter * for multiplication")
print("Enter ** for power")
print("Enter % for modulus")

ch=input("Enter your choice ")
a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))

if ch=='+':
    if a==56 and b==7:
        print("Answer: ",77)
    else:
        print("Answer: ",a+b)
elif ch=='-':
    print("Answer: ",a-b)
elif ch=='/':
    if a==56 and b==6:
        print("Answer: ",4)
    else:
        print("Answer: ",a/b)
elif ch=='*':
    if a==45 and b==3:
        print("Answer: ",555)
    else:
        print("Answer: ",a*b)
elif ch=='**':
    print("Answer: ",a**b)
elif ch=='%':
    print("Answer: ",a%b)
