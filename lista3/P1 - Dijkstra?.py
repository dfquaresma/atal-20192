# DESISTI DE FAZER EM GO...
n, m = map(int, input().split())

adjacencyMatrix  = {}
def updateMatrix(a, b, w):
  a_exist = adjacencyMatrix.get(a)
  b_exist = adjacencyMatrix.get(b)

  if a_exist and b_exist:
    a_and_b_know_each_other = a_exist.get(b)
    if a_and_b_know_each_other:
      w = min(w, adjacencyMatrix[a][b])
    adjacencyMatrix[a][b] = w
    adjacencyMatrix[b][a] = w

  else:
    if a_exist:
      adjacencyMatrix[a][b] = w
      adjacencyMatrix[b] = {a: w}

    elif b_exist:
      adjacencyMatrix[b][a] = w
      adjacencyMatrix[a] = {b: w}
    
    else:
      adjacencyMatrix[a] = {b: w}
      adjacencyMatrix[b] = {a: w}

predecessor      = {}
for i in range(m):
  a, b, w = map(int, input().split())
  updateMatrix(a, b, w)
  predecessor[a] = None
  predecessor[b] = None

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
from heapq import *
def extractMin():
  return heappop(h)

predecessor[1] = 1
distanceToRoot[1] = 0
heappush(h, (0, 1))
i = 0
while i < n:
  u = extractMin()
  uid = u[1]
  if used.get(uid):
    continue
  for nid, w in adjacencyMatrix[uid].items():
    if not used.get(nid):
      relax(uid, nid)
  used[u] = True
  i += 1

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
