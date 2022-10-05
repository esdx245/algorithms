from unittest import result


lista = [1, 1, 2, 2, 2, 8]
inlist = list(map(int, input().split()))
result = ""
for i in range(6):
    result += str(lista[i] - inlist[i])
    result += " "
result.rstrip()
print(result)
