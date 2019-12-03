# DESISTI DE FAZER EM GO...
from heapq import *
import traceback

try:
  n, m = map(int, input().split())
  adjacencyMatrix  = {}
  for i in range(1, n + 1):
    adjacencyMatrix[i] = {}
  for i in range(m):
    a, b, w = map(int, input().split())
    a, b, w = int(a), int(b), int(w)
    if not a in adjacencyMatrix[b] or adjacencyMatrix[b][a] > w:
      adjacencyMatrix[b][a] = w
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

  tmp = [None]
  predecessor[1] = 1
  distanceToRoot[1] = 0
  heappush(h, (0, 1))
  while len(h) > 0:
    u = heappop(h)
    uid = u[1]
    tmp += [uid]
    saw[uid] = True
    if not adjacencyMatrix.get(uid): continue
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

except Exception as error:
    just_the_string = traceback.format_exc()
    print(str(tmp[-1]) + " " + just_the_string)
