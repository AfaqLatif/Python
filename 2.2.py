from collections import defaultdict
class Graph:
   def __init__(self):
      self.graph = defaultdict(list)

   def edgeaddition(self,u,v):
      self.graph[u].append(v)

   def BFSA(self, s):
      visit = [False] * (max(self.graph) + 1)

      q = []
      q.append(s)

      visit[s] = True

      while q:
         s = q.pop(0)

         print (s, end = " ")
         for a in self.graph[s]:

            if visit[a]== False:
               q.append(a)
               visit[a] = True

g = Graph()
g. edgeaddition(1, 1)
g. edgeaddition(1, 2)
g. edgeaddition(2, 2)
g. edgeaddition(3, 2)
g. edgeaddition(2, 3)
g. edgeaddition(3, 1)
g. edgeaddition(3, 3)
print("The output of BFS : ")
g.BFSA(1)
