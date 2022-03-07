n,m = map(int,input().split())
lista = list(map(int,input().split()))
lista.sort(reverse = 1)
for i in range(m):
    lista[-2] = lista[-1] + lista[-2]
    lista[-1] = lista[-2]
    lista.sort(reverse = 1)
result = sum(lista)
print(result)