n = 9

def check(m, e, i, j): # complexity of O(n²). It could be O(n) with hashmap.
  for k in range(n):
    if m[i][k] == e:
      return False
  for k in range(n):
    if m[k][j] == e:
      return False
  
  si = 3 * (i // 3)
  sj = 3 * (j // 3)
  for ki in range(si, si + 3):
    for kj in range(sj, sj + 3):
      if m[ki][kj] == e:
        return False
  return True

m = [
  [   5,    3, None,   None,    7, None,   None, None, None], 
  [   6, None, None,      1,    9,    5,   None, None, None],
  [None,    9,    8,   None, None, None,   None,    6, None],
  
  [   8, None, None,   None,    6, None,   None, None,    3],
  [   4, None, None,      8, None,    3,   None, None,    1],
  [   7, None, None,   None,    2, None,   None, None,    6],
  
  [None,    6, None,   None, None, None,      2,    8, None],
  [None, None, None,      4,    1,    9,   None, None,    5],
  [None, None, None,   None,    8, None,   None,    7,    9]]

assert check(m, 2, 2, 0) == True
assert check(m, 4, 0, 2) == True
assert check(m, 7, 0, 8) == False # 7 already exists in that row
assert check(m, 8, 8, 0) == False # 8 already exists in that col
assert check(m, 5, 1, 1) == False # 5 already exists in that region
assert check(m, 2, 7, 7) == False # 2 already exists in that region

result = [
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None],
  [None, None, None, None, None, None, None, None, None]
]

def sudoku(m, i=0, j=0):
  if j == n: return

  if m[i][j] != None:
    if i < n-1:
      i += 1
    else:
      j += 1
      i = 0
    sudoku(m, i, j)
    return
  
  for e in range(1, n + 1):
    if check(m, e, i, j):
      m[i][j] = e
      if i < n-1:
        i += 1
      else:
        j += 1
        i = 0
      sudoku(m, i, j)

sudoku(result)
print(result)
