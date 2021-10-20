n = input()
if n[0] == "0":
  result = n.count("01")
else:
  result = n.count("10")
print(result)