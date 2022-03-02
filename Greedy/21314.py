n = input()
minv = ""
maxv = ""
count = 0
for i in range(len(n)):
  if n[i] == "M" :
    count += 1
  else:
    if count == 0:
      maxv += str(5)
    else :
      maxv += str(5*(pow(10,count)))
      minv += str(1*(pow(10,count-1)))
    count = 0
    minv += str(5)
if n[-1] == "M":
  maxv += str(1)*count
  minv += str(1*(pow(10,count-1)))

print(maxv)
print(minv)