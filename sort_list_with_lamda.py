#def sorted_list(l):
#    return l[1]

l=[[3,4],[1,2],[5,8]]
print("List before sorted ",l)

l.sort(key=lambda x: x[1])
print("List after sorted ",l)
