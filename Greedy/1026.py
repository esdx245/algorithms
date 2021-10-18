n = int(input())
lista = list(map(int,input().split()))
lista.sort()
listb = list(map(int,input().split()))
result = 0
for i in range(n):
  maxx = listb.pop(listb.index(max(listb)))
  result += lista[i] * maxx
print(result)
