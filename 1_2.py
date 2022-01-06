values=input("Enter the sequence number : ")
l=values. split(",")
t=tuple(l)
print(l)
print(t)
#l1=[]
#newlist = list(t)
#print(newlist)
tvalue=input("Enter the new value to update the list : ")
l[3]=tvalue

l1= l
print("New List : ",l1)
t1 = tuple(l1)
print("New Tuple : ",t1)
