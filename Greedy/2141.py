import sys
n = int(input())
allpopul  = 0
village =[]
for i in range(n):
  loca, people = map(int,sys.stdin.readline().split())
  allpopul += people
  village.append([loca,people])
if allpopul % 2 == 0:
  mid = allpopul/2
else :
  mid = allpopul/2 +1
if n == 1:
  result = village[0][0]
else:
  village.sort(key = lambda x : x[0])
  temp = 0
  for i in range(n):
    temp += village[i][1]
    if temp >= mid:
      result = village[i][0]
      break
print(result)