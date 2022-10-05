n = int(input())
m = int(input())
decimalsum = 0
decimalmin = 10000
if n == 1:
    n += 1

for i in range(n, m+1):
    decimal = False
    for j in range(2, i//2 + 1):
        if i % j == 0:
            decimal = True
            break
    if decimal == False:
        if decimalmin >= i:
            decimalmin = i
        decimalsum += i

if decimalsum == 0:
    print(-1)
else:
    print(decimalsum)
    print(decimalmin)
