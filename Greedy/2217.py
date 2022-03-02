n = int(input())
lista = []
for _ in range(n):
  lista.append(int(input()))
lista.sort()
max = 0
count = 0
for i in range(len(lista)):
  if (len(lista)-i) * lista[i] > max:
    max = (len(lista)-i) * lista[i]
    count = len(lista)-i
print(int(max/count))