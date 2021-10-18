n = int(input())
lista = []
for _ in range(n):
  lista.append(int(input()))
lista.sort()
for i in range(n):
  lista[i] *= (n-i)
print(max(lista))
