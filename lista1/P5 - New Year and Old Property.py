a, b = map(int, input().split(" "))
ab = str(bin(a)[2:])
bb = str(bin(b)[2:])

count_ab = 0
for e in ab:
  if e == "0":
    break
  count_ab += 1

count_bb = 0
for e in bb:
  if e == "0":
    break
  count_bb += 1

limark_count = 0
if len(ab) != len(bb):    
  for b in range(len(ab) + 1, len(bb)):
    limark_count += b - 1
  limark_count += len(ab) - count_ab
  limark_count += count_bb - 1

else:
  tmp = 0
  for i in range(ab):
    if ab[i] != bb[i]:
      tmp = i
      break
  
  if tmp == 0:
    limark_count = tmp
  else:
    print()
    
print(limark_count)
