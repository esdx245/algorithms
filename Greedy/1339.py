n = int(input())
lista = [[] for _ in range(8)]
alpha = dict()
for i in range(65,91):
  alpha[chr(i)] = 0
for i in range(n):
  temp = input()
  inputt = (8-len(temp))*" "+temp
  for i in range(8):
    lista[i].append(inputt[i])
for i in range(8):
  for j in range(len(lista[i])):
    if lista[i][j] != ' ':
      alpha["{}".format(lista[i][j])] += 1*pow(10,7-i)
alpha = list(alpha.values())
alpha.sort(reverse = 1)
result = 0
for i in range(10):
  result += alpha[i]*(9-i)
print(result)