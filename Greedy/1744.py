n = int(input())
list0,listminus,listplus=[],[],[]
result = 0
for i in range(n):
  temp = int(input())
  if temp == 0:
    list0.append(temp)
  elif temp == 1:
    result += 1
  elif temp > 1:
    listplus.append(temp)
  else:
    listminus.append(temp)
listminus.sort()
listplus.sort(reverse = 1)
if len(listminus) %2 == 1:
  if len(list0) != 0:
    result += 0*listminus.pop()
  else:
    result += listminus.pop()
if len(listplus) %2 == 1:
  result += listplus.pop()
for i in range(0,len(listminus),2):
  result += listminus[i]*listminus[i+1]
for i in range(0,len(listplus),2):
  result += listplus[i]*listplus[i+1]
print(result)