import sys
n = int(input())
lista = list(map(int, sys.stdin.readline().split()))
maxval = 0
s = []
s.append(lista[0])
for i in range(1,n):
  s.append(s[i-1] + lista[i])

#case1 벌벌꿀 경우
for i in range(1,n-1):
  temp = s[-1] - s[0] - lista[i] + s[-1] - s[i]
  if temp > maxval:
    maxval = temp

#case2 꿀벌벌 경우
for i in range(1,n-1):
  temp = s[-2] - lista[i]*2 + s[i]
  if temp > maxval:
    maxval = temp
#case3 벌꿀벌 경우
temp = s[-1] - lista[0] - lista[-1] + max(lista[1:n-1])
if temp > maxval :
  maxval = temp
print(maxval)