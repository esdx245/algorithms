a, b = map(int, input().split())
c = int(input())
if b+c >= 60:
    tempa = a + ((b+c) // 60)
else:
    tempa = a
tempb = (b+c) % 60
if tempa >= 24:
    tempa -= 24
print(tempa, tempb)
