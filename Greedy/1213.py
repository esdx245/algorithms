n = input()
count = [0]*26
result = ""
for i in range(len(n)):
  count[ord(n[i])-65] += 1
forword = ""
backword = ""
mid = ""
for i in range(len(count)):
  if count[i] != 0 and count[i] %2 == 1:
    if len(mid) == 0:
      mid = chr(65+i)
      forword += chr(65+i) *(count[i]//2)
      backword = chr(65+i) *(count[i]//2) + backword
    else:
      result = -1
  else :
    forword += chr(65+i) *(count[i]//2)
    backword = chr(65+i) *(count[i]//2) + backword
if result != -1:
  result = forword + mid +backword
else :
  result = "I'm Sorry Hansoo"
print(result)