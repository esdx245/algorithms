n = int(input())
result = 0
if n in (1,3):
  result = -1
else:
  if n %2 == 0:
    if n < 10 :
      result += n //2
    else:
      result += (n // 10) * 2
      result += n % 10 // 2
  else :
    if n % 5 == 0:
      result += n // 5
    else:
      if n < 15 :
        result += 1
        result += (n-5) // 2
      else :
        if n % 10 < 5:
          result += (n // 5) -1
          result += (n%5+5) // 2
        else :
          result += n //5
          result += (n%5) // 2
print(result)