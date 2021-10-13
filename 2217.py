n = int(input())
lista = []
for _ in range(n):
  lista.append(int(input()))
minn = min(lista)
maxx = max(lista)
if minn * n > maxx:
  print(minn*n)
else:
  print(maxx)
