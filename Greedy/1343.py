n = list(input())
count = []
temp = 0
result = ""
for i in n:
  if i == "X":
    temp += 1
  else :
    if temp % 2 == 1:
      result = str(-1)
      break;
    else:
      count.append(temp)
      count.append(-1)
      temp = 0
if n[-1] == "X" :
  if temp % 2 == 1:
    result = str(-1)
  else:
    count.append(temp)
if result != "-1":
  for i in range(len(count)):
    if count[i] == -1:
      result += "."
    else:
      if count[i] == 0:
        pass
      elif count[i] % 4 ==0:
        result += "AAAA" * (count[i] // 4)
      else :
        result += ("AAAA" * (count[i]//4)) + ("BB" * (count[i]%4 // 2))
print(result)