n = int(input())
timelist = list(map(int,input().split()))
timelist.sort()
result = timelist[0]
for i in range(0,len(timelist)-1):
  timelist[i+1] += timelist[i]
  result += timelist[i+1]
print(result)
