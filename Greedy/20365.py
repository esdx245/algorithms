n = int(input())
color = input()
result = 0
if color[0] == "B":
  result = color.count("BR") + 1
else:
  result = color.count("RB") + 1
print(result)