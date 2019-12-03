# DESISTI DE FAZER EM GO...
from heapq import *
n, m = map(int, input().split())
 
adjacencyMatrix  = {}
for i in range(m):
  a, b, w = map(int, input().split())
  if not adjacencyMatrix.get(b): adjacencyMatrix[b] = {}
  if not a in adjacencyMatrix[b] or adjacencyMatrix[b][a] > w:
    adjacencyMatrix[b][a] = w
  if not adjacencyMatrix.get(a): adjacencyMatrix[a] = {}
  if not b in adjacencyMatrix[a] or adjacencyMatrix[a][b] > w:
    adjacencyMatrix[a][b] = w
 
predecessor = {}
for i in range(1, n + 1):
    predecessor[i] = None
 
h = []
distanceToRoot   = {}
def relax(u, v):
  distanceToRootFromU = distanceToRoot.get(u)
  if distanceToRootFromU == None:
    distanceToRootFromU = float('inf')
  distanceThroughU = distanceToRootFromU + adjacencyMatrix[u][v]
 
  distanceToRootFromV = distanceToRoot.get(v)
  if distanceToRootFromV == None:
    distanceToRootFromV = float('inf')
 
  if distanceToRootFromV > distanceThroughU:
    distanceToRoot[v] = distanceThroughU
    predecessor[v] = u
    heappush(h, (distanceThroughU, v))
 
used = {}
predecessor[1] = 1
distanceToRoot[1] = 0
heappush(h, (0, 1))
while len(h) > 0:
  u = heappop(h)
  uid = u[1]
  if used.get(uid):
    continue
  for nid, _ in adjacencyMatrix[uid].items():
    if not used.get(nid):
      relax(uid, nid)
  used[u] = True
 
output = str(n)
nod = predecessor[n]
while nod != 1 and nod != None:
  output = str(nod) + " " + output
  nod = predecessor[nod]
output = "1 " + output
 
if nod != None:
  print(output)
else:
  print("-1")
