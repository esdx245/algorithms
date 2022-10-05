n, m = map(int, input().split())

for i in range(n, m+1):
    decimal = False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            decimal = True
            break
    if decimal == False:
        if i != 1:
            print(i)
