f=open("files.txt","r+")

#data=f.read()
#print(data)

for x in f:
    print(x , end="")

f.write("Thanks")

#print(f.readlines())

f.close()