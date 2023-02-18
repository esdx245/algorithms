
n, k = map(int, input().split())
count = 0
for h in range(0, n+1):
    if h < 10:
        hour = '0' + str(h)
    else:
        hour = str(h)
    if str(k) in hour:
        count += 3600
    else:
        for m in range(0, 60):
            if m < 10:
                minute = '0' + str(m)
            else:
                minute = str(m)
            if str(k) in minute:
                count += 60
            else:
                for s in range(0, 60):
                    if s < 10:
                        second = '0' + str(s)
                    else:
                        second = str(s)
                    if str(k) in second:
                        count += 1

print(count)
