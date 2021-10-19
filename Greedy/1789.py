s = int(input())
count = 1
while 1:
  if count > s:
    count -= 1
    print(count)
    break
  s -= count
  count += 1