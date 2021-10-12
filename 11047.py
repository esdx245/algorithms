n,k = map(int,input().split())
coin = []
count = 0
for _ in range(n):
  coin.append(int(input()))
for i in range(n-1,-1,-1):
  if k >= coin[i]:
    temp = k // coin[i]
    k -= temp * coin[i]
    count += temp
    temp = 0
  if k == 0:
    print(count)
    break

