n = int(input())
lista = [999999]
result = 0
for _ in range(n):
  lista.append(int(input()))
lista.sort(reverse = 1)
if n % 3 == 1:
  result += lista.pop()
elif n % 3 == 2:
  result += lista.pop()
  result += lista.pop()
if n >=3:
  for i in range(1,len(lista)-1):
    if i % 3 != 0:
      result += lista[i]
  print(result)
else :
  print(result)