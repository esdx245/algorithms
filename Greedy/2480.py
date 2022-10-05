inputt = list(map(int, input().split()))
dicta = dict()
tic = 0
for i in inputt:
    dictkey = list(dicta.keys())
    for j in range(len(dictkey)):
        if i == dictkey[j]:
            dicta[dictkey[j]] += 1
            tic = 1
            break
    if tic == 0:
        dicta[i] = 1
    tic = 0
dictkey = list(dicta.keys())
if len(dictkey) == 3:
    result = max(inputt) * 100
elif len(dictkey) == 2:
    temp = 0
    for i in dictkey:
        if temp < dicta[i]:
            temp = dicta[i]
            r = i
    result = 1000 + 100*r
else:
    result = 10000 + inputt[0] * 1000
print(result)
