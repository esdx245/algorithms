import itertools

n = int(input())
k = int(input())
temp = []
for i in range(n):
    temp.append(int(input()))

combi = list(itertools.permutations(temp, k))
result = set()
for i in combi:
    t = ""
    for j in range(k):
        t += str(i[j])
    result.add(t)
print(len(result))
