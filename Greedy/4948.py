lista = []
for i in range(2, 246913):
    d = False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            d = True
            break
    if d == False:
        lista.append(i)

while 1:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in lista:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)
