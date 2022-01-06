from collections import defaultdict
class Graph:
   def __init__(self):
      self.graph = defaultdict(list)

   def edgeaddition(self, u, v):
      self.graph[u].append(v)

   def DFSUtil(self, v, visit):
      visit.add(v)
      print(v, end=' ')

      for neighbour in self.graph[v]:
         if neighbour not in visit:
            self.DFSUtil(neighbour, visit)

   def DFSA(self, v):

      visit = set()

      self.DFSUtil(v, visit)
g = Graph()
g. edgeaddition(1, 1)
g. edgeaddition(1, 2)
g. edgeaddition(2, 2)
g. edgeaddition(3, 2)
g. edgeaddition(2, 3)
g. edgeaddition(3, 1)
g. edgeaddition(3, 3)

print("The output of DFS : ")
g.DFSA(1)
