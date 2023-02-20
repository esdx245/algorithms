import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
ice = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    i1, i2 = map(int, input().split())
    ice[i1-1][i2-1] = 1
    ice[i2-1][i1-1] = 1


result = 0
combi = list(itertools.combinations(range(n), 3))
for i in combi:
    if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
        continue
    result += 1
print(result)
