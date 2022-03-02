n = int(input())
lista = list(map(int, input().split()))
lista.sort(reverse = 1)
result = lista[0]
for i in range(1, n):
  if result < lista[i]:
    result = lista[i] + result / 2
  else:
    result += lista[i] / 2
if result - int(result) == 0:
  result = int(result)
print(result)