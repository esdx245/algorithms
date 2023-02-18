import itertools

n, s = map(int, input().split())
temp = list(map(int, input().split()))
count = 0

for i in temp:
    if i == s:
        count += 1

combi_temp = []
for i in range(2, n+1):
    combi_temp += list(itertools.combinations(temp, i))
for i in combi_temp:
    if sum(i) == s:
        count += 1

print(count)
