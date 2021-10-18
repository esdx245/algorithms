n = int(input())
lista = list(map(int,input().split()))
lista.sort()
count = 0
idd = 0
for i in lista:
  if count+1 >= i:
    count += i
    idd += 1
    if idd == n:
      print(count+1)
  else:
    print(count + 1)
    break
