import sys
t = int(input())
result = []
for i in range(t):
  n = int(sys.stdin.readline().rstrip())
  lista = []
  count = 1
  for j in range(n):
    x,y = map(int,sys.stdin.readline().split())
    lista.append((x,y))
  lista.sort()
  minn = lista[0][1]
  for i in range(1,n):
    if lista[i][1] < minn:
      count += 1
      minn = lista[i][1]
  result.append(count)
for _ in result:
  print(_)
