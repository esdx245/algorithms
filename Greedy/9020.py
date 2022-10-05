lista = []
for i in range(2, 10000):
    d = False
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            d = True
            break
    if d == False:
        lista.append(i)
T = int(input())
for _ in range(T):
    n = int(input())
    tempa = n//2
    tempb = n//2
    for i in range(n//2, 1, -1):
        if tempa in lista and tempb in lista:
            print(tempa, tempb, sep=" ")
            break
        else:
            tempa -= 1
            tempb += 1
