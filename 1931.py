n = int(input())
lista = []
result = []
for _ in range(n):
  x,y = map(int,input().split())
  lista.append((x,y))
lista.sort(key = lambda x : (x[1],x[0]))
for start, end in lista:
  if len(result) == 0:
    result.append((start,end))
  elif result[-1][1] <= start:
    result.append((start,end))
print(len(result))
