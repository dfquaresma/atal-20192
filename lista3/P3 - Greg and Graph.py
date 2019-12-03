
n = int(input())
adjacency_matrix = []
for i in range(n):
  row = list(map(int, input().split()))
  adjacency_matrix.append(row)
vs = list(map(int, input().split()))
 
deleted = [False] * (n)
def floyd_warshall(w):
  n = len(w)
  d = list(map(list, w))
  for k in range(n):
    if deleted[k]: continue
    for i in range(n):
      if deleted[i]: continue
      for j in range(n):
        if deleted[j]: continue
        d[i][j] = min(d[i][j], d[i][k] + d[k][j])
  return d
 
output = []
for e in vs:
  d = floyd_warshall(adjacency_matrix)
  s = 0
  for row in range(n):
    if deleted[row]: continue
    for col in range(n):
      if deleted[col]: continue
      s += d[row][col]
  output += [s]
  deleted[e - 1] = True
 
print(" ".join(map(str, output)))
