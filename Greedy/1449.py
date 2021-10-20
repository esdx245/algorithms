n,l = map(int,input().split())
lista = list(map(int,input().split()))
lista.sort()
result = 1
start = lista[0]-0.5
end = start + l
for i in range(n):
  if end > lista[i] > start:
    continue
  else:
    result += 1
    start = lista[i] - 0.5
    end = start +l
print(result)