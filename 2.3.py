from collections import defaultdict
class Graph:
   def __init__(self,vertices):
      self.V = vertices
      self.graph = defaultdict(list)

   def edgeaddition(self,u,v):

      self.graph[u].append(v)

   def DLS(self,src,target,maxDepth):
      if src == target : return True

      if maxDepth <= 0 : return False

      for i in self.graph[src]:
            if(self.DLS(i,target,maxDepth-1)):
               return True
      return False

   def IDDFS(self,src, target, maxDepth):
      for i in range(maxDepth):
         if (self.DLS(src, target, i)):
            return True
      return False

g = Graph (5);
g. edgeaddition(1, 1)
g. edgeaddition(1, 2)
g. edgeaddition(2, 2)
g. edgeaddition(3, 2)
g. edgeaddition(2, 3)
g. edgeaddition(3, 1)
g. edgeaddition(3, 3)

target = 3; maxDepth = 3; src = 1
if g.IDDFS(src, target, maxDepth) == True:

   print ("Target is reachable " + "within max depth")

else :
   print ("Target is not reachable " + "within max depth")
