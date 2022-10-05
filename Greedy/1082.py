n = int(input())
temp = list(map(int, input().split()))
price = []
result = ""
for i in range(n):
    count = 0
    for j in range(len(price)):
        if price[j][0] == temp[i]:
            price[j][1].append(i)
            break
        count += 1
    if count == len(price):
        price.append([temp[i], [i]])
m = int(input())
price.sort()
if len(price) == 1:
    print(str(price[0][-1][-1])*(m//price[0][0]))
else:
    maxlen = m//price[0][0]
    count = len(price)-1
    while(1):
        if count == 0:
            result += str(price[count][1][-1]) * maxlen
            break
        print(price[count][0])
        print(price[0][0]*(maxlen-1))
        print()
        if price[count][0] + (price[0][0]*(maxlen-1)) <= m:
            if price[count][1][-1] == 0 and maxlen == m//price[0][0]:
                count -= 1
            else:
                result += str(price[count][1][-1])
                maxlen -= 1
        else:
            count -= 1
    print(result)
