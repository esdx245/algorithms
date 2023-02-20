
n, m = map(int, input().split())
count_a = [0 for _ in range(m)]
count_t = [0 for _ in range(m)]
count_g = [0 for _ in range(m)]
count_c = [0 for _ in range(m)]
for i in range(n):
    temp = input()
    for j in range(m):
        if temp[j] == "A":
            count_a[j] += 1
        elif temp[j] == "T":
            count_t[j] += 1
        elif temp[j] == "G":
            count_g[j] += 1
        else:
            count_c[j] += 1

result = ""
count = 0
for _ in range(m):
    t = max(count_a[_], count_c[_], count_g[_], count_t[_])
    if t == count_a[_]:
        result += "A"
    elif t == count_c[_]:
        result += "C"
    elif t == count_g[_]:
        result += "G"
    else:
        result += "T"
    count += n-t

print(result)
print(count)
