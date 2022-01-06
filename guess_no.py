n=81                                                   # No. to guess
print("Enter number between 0 and 100")
print("You can guess the number only 9 times..")
x=1
while(x<10):
    nmbr=int(input("Enter number to guess : "))
    if(nmbr<n):
        print("You entered less number..Enter number again ")
    elif(nmbr>n):
        print("You entered greater number..Enter number again ")
    elif(nmbr==n):
        print("You entered correct number..Congratulations")
        print(9-x,"number of guesses left")
        break
    else:
        print("Error..you fail to guess the number")
    x=x+1
    if(x==10):
        print("Game Over")
        print("You fail to gues the nmbr in given nmbr of guesses.")

#print("Game Over")
#print("You fail to gues the nmbr in given nmbr of guesses.")