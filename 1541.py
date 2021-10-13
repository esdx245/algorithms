n = input()
lista = n.split("-")
for i in range(len(lista)):
  if lista[i].count("+") != 0:
    temp = lista[i].split("+")
    tempresult = 0
    for j in temp:
      tempresult += int(j)
    lista[i] = tempresult
result = int(lista[0])
for i in range(1,len(lista)):
  result -= int(lista[i])
print(result)
