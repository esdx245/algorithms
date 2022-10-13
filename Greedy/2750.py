n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
lista.sort()
for i in range(n):
    print(lista[i])

# n = int(input())
# lista = []

# for i in range(n):
#     lista.append(int(input()))
#     if i >= 1 and lista[i-1] > lista[i]:
#         temp = lista[i]
#         lista[i] = lista[i-1]
#         lista[i-1] = temp

# 이렇게 입력을 받으면서 비교해서 하는 것보다
# 입력을 한번에 다 받고 아래에서 range를 n-1로 변경하는 것이 더 빠르다!!

# for i in range(n-2):
#     for j in range(1, n):
#         if lista[j-1] > lista[j]:
#             temp = lista[j]
#             lista[j] = lista[j-1]
#             lista[j-1] = temp
# for i in range(n):
#     print(lista[i])
