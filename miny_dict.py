dict={"append":"add something at the end of list",
    "update":"add something in dictionary",
    "5":"five",
    "A":"Allah SWT",
    "B":"Bismillah",
    "C":"Caligraphy",
    "D":"Dua",
    "E":"Emaan",
    "F":"Fazle-Kareem",
    "R":"Rahman",
    "K":"Kareem",
    "reverse":"we can reverse the list through slicing"}

print(dict.keys())
print("Choose from above keys to see the meaning...")

x=input("Enter key : ")
print("Suggestion for ",x," : ",dict[x])
