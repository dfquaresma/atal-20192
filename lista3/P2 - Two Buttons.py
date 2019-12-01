(n , m), b = map(int, input().split()), 0

def m_is_even(m):
  return m % 2 == 0

if n == m:
  print(b)

else:
  while m > n:
    b += 1
    if m_is_even(m) and m > n:
      m -= m // 2
      continue
    m += 1
  while n > m:
    b += 1
    m += 1
  print(b)
