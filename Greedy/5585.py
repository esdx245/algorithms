lista = [500, 100, 50, 10, 5, 1]
money = int(input())
count = 0
rest = 1000-money
result = 0
while(1):
    if count >= 6:
        break
    if rest // lista[count] != 0:
        result += rest // lista[count]
        rest -= (rest // lista[count]) * lista[count]
        count += 1
    else:
        count += 1
print(result)
