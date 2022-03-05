import sys
n, k = map(int,input().split())
num = sys.stdin.readline().rstrip()
count = 0
stack = []
for i in range(n):
  while count < k and stack and int(stack[-1]) < int(num[i]):
    stack.pop()
    count += 1
  stack.append(num[i])
print(''.join(stack[:n-k]))