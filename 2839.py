n = int(input())
count5,count3,count = 9999999,9999999,0
if n % 5 == 0:
    count5 = n //5
if n % 3 == 0:
  if n % 15 == 0:
    temp = ncount3 = n // 5
    temp -= n/5 * 5
    count3 += temp // 3
  else:
    count3 = n // 3
while 1:
  if n % 5 == 0:
    count += n // 5
    break
  elif n < 3:
    count = -1
    n = 0
    break
  else:
    count += 1
    n -= 3
print(min(count5,count3,count))
