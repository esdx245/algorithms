n = input()
result = ""
for i in range(len(n)):
  if n[i] == "0":
    if i == 0:
      result += "0"
    else:
      result += "000"
  elif n[i] == "1":
    if i == 0:
      result += "1"
    else:
      result += "001"
  elif n[i] == "2":
    if i == 0:
      result += "10"
    else:
      result += "010"
  elif n[i] == "3":
    if i == 0:
      result += "11"
    else:
      result += "011"
  elif n[i] == "4":
    result += "100"
  elif n[i] == "5":
    result += "101"
  elif n[i] == "6":
    result += "110"
  elif n[i] == "7":
    result += "111"
print(result)