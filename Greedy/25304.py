price = int(input())
num = int(input())
temp = 0
for i in range(num):
    a, b = map(int, input().split())
    temp += a*b
if temp == price:
    print("Yes")
else:
    print("No")
