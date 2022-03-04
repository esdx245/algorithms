import sys
sensor = int(input())
base = int(input())
location = list(map(int, sys.stdin.readline().split()))
location.sort()
temp = []
for i in range(1,sensor):
  temp.append(location[i]-location[i-1])
temp.sort()
result = sum(temp[:(sensor-1)-(base-1)])
print(result)