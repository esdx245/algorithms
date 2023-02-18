import itertools

n, m = map(int, input().split())
t_list = list(map(int, input().split()))

temp = list(itertools.combinations(t_list, 3))
temp_close = 0
for i in range(len(temp)):
    if m - sum(temp[i]) == 1:
        temp_close = m
        break
    if temp_close < sum(temp[i]) < m:
        temp_close = sum(temp[i])
print(temp_close)
