l1 = ["HDD", "SDD", "RAM", "Laptop"]

i = 0
for item in l1:
    if i%2 != 0:
        print(f"Jarvis please buy {item}")
    i += 1

print("Lets try it using enumerate function")
for index, item in enumerate(l1):                        #here indexing start from 0
    if index%2==0:
        print(f"Jarvis please buy {item}")
