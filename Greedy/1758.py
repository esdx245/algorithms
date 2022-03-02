n = int(input())
lista = []
result = 0
for _ in range(n):
  lista.append(int(input()))
lista.sort(reverse = 1)
for i in range(n):
  temp = lista[i] - i
  if temp > 0:
    result += temp
    temp = 0
  else:
    temp = 0
print(result)