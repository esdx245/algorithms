
a = int(input())
t = int(input())
guho = int(input())
temp = []
bun = daegi = 1
cycle = 0

while 1:
    cycle += 1
    prev_bun = bun

    for _ in range(2):
        temp.append((bun, 0))
        bun += 1
        temp.append((daegi, 1))
        daegi += 1
    for _ in range(cycle+1):
        temp.append((bun, 0))
        bun += 1
    for _ in range(cycle+1):
        temp.append((daegi, 1))
        daegi += 1
    if prev_bun < t <= bun:
        print(temp.index((t, guho)) % a)
        break
