a = int(input())
count = 1
tempa, tempb = 0, 0
while 1:
    if a > count:
        a -= count
        count += 1
    if a <= count:
        if count % 2 == 0:
            if a == 1:
                tempa = 1
                tempb = count
            elif a == count:
                tempa = a
                tempb = 1
            else:
                tempa = a
                tempb = count+1 - a
        else:
            if a == 1:
                tempa = count
                tempb = 1
            elif a == count:
                tempa = 1
                tempb = a
            else:
                tempa = count+1 - a
                tempb = a
        break
print(f"{tempa}/{tempb}")
