n = int(input())
lista = list(map(int,input().split()))
lista.sort()
maxval = 0
if n % 2 == 1:
  maxval = lista.pop()
  n -= 1
listb = lista
for i in range(int(n/2)):
  if maxval < lista[i] + listb[n-i-1]:
    maxval = lista[i] + listb[n-i-1]
print(maxval)