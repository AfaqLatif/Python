List = [1,2,3,4]
print("List before swapping of elements : ", List)
position1 = int(input("Enter element, which you want to swap : "))
position2 = int(input("Enter element, which you want to swap : "))

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

print("List after swapping of elements : ", swapPositions(List, position1 - 1, position2 - 1))
