# DESISTI DE FAZER EM GO...
from heapq import *

n, m = map(int, input().split())
adjacency_list = [[]]
distanceToRoot = [float("inf")]
predecessor = [None]
for i in range(1, n + 1):
  adjacency_list.append([])
  distanceToRoot.append(float("inf"))
  predecessor.append(None)

for i in range(m):
  a, b, w = map(int, input().split())
  adjacency_list[a].append((b, w))
  adjacency_list[b].append((a, w))

min_heap = []
distanceToRoot[1] = 0
heappush(min_heap, (0, 1))
while min_heap:
  distanceToRootFromU, uid = heappop(min_heap)
  for vid, weight in adjacency_list[uid]:
      distanceThroughU = distanceToRootFromU + weight
      if distanceToRoot[vid] > distanceThroughU:
        distanceToRoot[vid] = distanceThroughU
        predecessor[vid] = uid
        heappush(min_heap, (distanceThroughU, vid))

nod = n
output_list = []
while nod != 1 and nod != None:
  output_list += [nod]
  nod = predecessor[nod]

if nod != None:
  output_list += [nod]
  output_list.reverse()
  print(' '.join(map(str, output_list)))
else:
  print("-1")
