n = int(input())
lista= []
for i in range(n):
    lista.append(int(input()))
tempmax = lista[-1]
count = 0
for i in range(n-2,-1,-1):
    if lista[i] >= tempmax:
        temp = lista[i] -tempmax +1
        count += temp
        lista[i] -= temp
    tempmax = lista[i]
print(count)