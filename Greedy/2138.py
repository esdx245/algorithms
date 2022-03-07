import sys, copy
n = int(input())
a1 = list(map(int,sys.stdin.readline().rstrip()))
a2 = list(map(int,sys.stdin.readline().rstrip()))
case1 = copy.deepcopy(a1)
case2 = copy.deepcopy(a1)

def twoswap(st,n):
  st[n] = abs(st[n]-1)
  st[n+1] = abs(st[n+1]-1)
def threeswap(st,n):
  st[n-1] = abs(st[n-1]-1)
  st[n] = abs(st[n]-1)
  st[n+1] = abs(st[n+1]-1)
result = 0
for i in range(2):
  count = 0
  if a1 == a2:
    result = 0
    break
  if i == 0:
    for j in range(n):
      if j == 0:
        twoswap(case1,j)
        count += 1
      else:
        if case1[j-1] != a2[j-1]:
          if j == n-1:
            twoswap(case1, j-1)
            count += 1
          else:
            threeswap(case1,j)
            count += 1
    if case1[-1] == a2[-1]:
      result = count
      break
  else:
    for j in range(1,n):
      if case2[j-1] != a2[j-1]:
        if j == n-1:
          twoswap(case2, j-1)
          count += 1
        else:
          threeswap(case2, j)
          count += 1
    if case2[-1] != a2[-1]:
      result = -1
    else :
      result = count
print(result)