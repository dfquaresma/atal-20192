# DESISTI DE FAZER EM GO...
n, m = map(int, input().split())

adjacencyMatrix  = [[0] * (n + 1) for _ in range(n+1)]
distanceToRoot   = [float('inf') for _ in range(n+1)]
predecessor      = [None for _ in range(n+1)]
used             = [False for _ in range(n+1)]

def updateMatrix(a, b, w):
  if adjacencyMatrix[a][b] != 0:
    w = min(w, adjacencyMatrix[a][b])
  adjacencyMatrix[a][b] = w
  adjacencyMatrix[b][a] = w

for i in range(m):
  a, b, w = map(int, input().split())
  updateMatrix(a, b, w)

def relax(u, v):
  distanceThroughU = distanceToRoot[u] + adjacencyMatrix[u][v]
  if distanceToRoot[v] > distanceThroughU:
    distanceToRoot[v] = distanceThroughU
    predecessor[v] = u

distanceToRoot[1] = 0
predecessor[1] = 1
def extractMin():
  idOfTheMin = 0
  for i in range(n):
    if not used[i] and distanceToRoot[i] < distanceToRoot[idOfTheMin]:
      idOfTheMin = i
  return idOfTheMin

for i in range(n):
  u = extractMin()
  for j in range(1, n + 1):
      if used[j] == False and adjacencyMatrix[u][j] != 0:
        relax(u, j)
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
