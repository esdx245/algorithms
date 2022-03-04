import sys
n, k = map(int,input().split())
lista = list(map(int, sys.stdin.readline().split()))
temp = []
for i in range(n-1):
  temp.append(lista[i+1] - lista[i])
temp.sort()
result = sum(temp[:n-k])
print(result)