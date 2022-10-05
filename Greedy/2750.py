n = int(input())
lista = [0, 1001]
for i in range(n):
    temp = int(input())
    mid = len(lista)//2
    while 1:
        if lista[mid] < temp < lista[mid+1]:
            templist = lista[:mid+1]
            templist.append(temp)
            lista = templist + lista[mid+1:]
            break
        elif lista[mid] > temp:
            mid = mid//2
        else:
            mid += mid // 2

for _ in range(1, n+1):
    print(lista[_])
