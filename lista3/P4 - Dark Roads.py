father = []
def find(nodeIndex):
    if father[nodeIndex] == nodeIndex:
      return nodeIndex
    father[nodeIndex] = find(father[nodeIndex])
    return father[nodeIndex]

rank   = []
def union(nodeAIndex, nodeBIndex):
    nodeAIndex = find(nodeAIndex)
    nodeBIndex = find(nodeBIndex)
    if rank[nodeAIndex] < rank[nodeBIndex]:
      nodeAIndex, nodeBIndex = nodeBIndex, nodeAIndex
    rank[nodeAIndex] += rank[nodeBIndex]
    father[nodeBIndex] = father[nodeAIndex]

edges = []
def kruskal(m, n):
  edges.sort(key=lambda tup: tup[2])
  minimumCoverTreeSum = 0
  for e in edges:
    if find(e[0]) != find(e[1]):
      union(e[0], e[1])
      minimumCoverTreeSum += e[2]
  return minimumCoverTreeSum

while True:
  m, n = map(int, input().split())
  if m == 0 and n == 0: break
  edges = []
  total = 0
  for i in range(n):
    x, y, z = map(int, input().split())
    edges.append((x, y, z))
    total += z

  father = [0]
  rank   = [0]
  for i in range(1, m + 1):
    father.append(i)
    rank.append(i)

  minimumCoverTreeSum = kruskal(m, n)
  print(str(total - minimumCoverTreeSum))
