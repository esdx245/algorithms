n = int(input())
listroad = list(map(int,input().split()))
listoil = list(map(int,input().split()))
count = 1
ex = 0
price = 0
while 1:
  if listoil[ex] > listoil[count]:
    price += sum(listroad[ex:count])*listoil[ex]
    ex = count
  else:
    count += 1
  if count == n:
    if listoil[ex] <= listoil[count -1]:
      price += sum(listroad[ex:count]) * listoil[ex]
      print(price)
      break
