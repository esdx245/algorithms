import itertools

n, m = map(int, input().split())
t_list = [list(map(int, input().split())) for _ in range(n)]

combi = list(itertools.combinations(range(m), 3))
maxsum = 0
for a, b, c in combi:
    tmpsum = 0
    for i in range(n):
        tmpsum += max(t_list[i][a], t_list[i][b], t_list[i][c])
    maxsum = max(tmpsum, maxsum)
print(maxsum)
