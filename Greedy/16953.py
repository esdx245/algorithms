a,b = map(int,input().split())
cannot = [3,5,7,9]
result = 1

while 1:
  if a == b:
    break
  if b%10 in cannot:
    result = -1
    break
  elif b < 2*a:
    result = -1
    break
  elif b % 10 == 1:
    b -= 1
    b//= 10
    result += 1
  elif  b %2 == 0:
    b //= 2
    result += 1
print(result)