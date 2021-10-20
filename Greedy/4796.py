lista = []
while 1:
  lista.append(list(map(int,input().split())))
  if lista[-1] == [0,0,0]:
    break
for i in range(len(lista)-1):
  allweek = lista[i][2] // lista[i][1]
  restday = lista[i][2] % lista[i][1]
  result = allweek * lista[i][0]
  if restday >= lista[i][0]:
    result += lista[i][0]
  else:
    result += restday
  print("Case {}: {}".format(i+1,result))