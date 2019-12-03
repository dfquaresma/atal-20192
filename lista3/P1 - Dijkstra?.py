# DESISTI DE FAZER EM GO...
from heapq import *
n, m = map(int, input().split())

adjacencyMatrix  = {}
for i in range(m):
  a, b, w = map(int, input().split())
  if a == b: continue
  if not adjacencyMatrix.get(b): adjacencyMatrix[b] = {}
  if not a in adjacencyMatrix[b] or adjacencyMatrix[b][a] > w:
    adjacencyMatrix[b][a] = w
  if not adjacencyMatrix.get(a): adjacencyMatrix[a] = {}
  if not b in adjacencyMatrix[a] or adjacencyMatrix[a][b] > w:
    adjacencyMatrix[a][b] = w

saw = {}
predecessor = {}
distanceToRoot = {}
for i in range(1, n + 1):
    predecessor[i] = None
    distanceToRoot[i] = float('inf')
    saw[i] = False

h = []
def relax(u, v):
  distanceThroughU = distanceToRoot[u] + adjacencyMatrix[u][v]
  if distanceToRoot[v] > distanceThroughU:
    distanceToRoot[v] = distanceThroughU
    predecessor[v] = u
    heappush(h, (distanceThroughU, v))

predecessor[1] = 1
distanceToRoot[1] = 0
heappush(h, (0, 1))
while len(h) > 0:
  u = heappop(h)
  uid = u[1]
  saw[uid] = True
  for nid, _ in adjacencyMatrix[uid].items():
    if not saw[nid]:
      relax(uid, nid)

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
