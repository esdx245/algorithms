import heapq, sys
n = int(input())
for _ in range(n):
  heap = []
  m = int(input())
  lista = list(map(int, sys.stdin.readline().split()))
  lista.sort()
  print(lista[0], lista[-1], sep=" ")