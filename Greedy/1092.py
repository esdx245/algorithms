import sys
n = int(input())
crain = list(map(int,sys.stdin.readline().split()))
crain.sort(reverse = 1)
m = int(input())
box = list(map(int,sys.stdin.readline().split()))
box.sort(reverse = 1)
for i in range(n):
  crain[i] = [crain[i],0]
maxlen = 0
rotate = 0
if box[0] > crain[0][0]:
    maxlen = -1
else : 
  for i in range(m):
    crain.sort(key = lambda x : x[1])
    for j in range(n):
      if box[i] <= crain[j][0]:
        crain[j][1] = int(crain[j][1]) + 1
        if maxlen < crain[j][1]:
          maxlen = crain[j][1]
        break
print(maxlen)
