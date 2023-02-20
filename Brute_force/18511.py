import itertools

n, k = map(int, input().split())
target = tuple(map(int, str(n)))
temp = tuple(map(int, input().split()))

combi1 = list(itertools.product(temp, repeat=len(str(n))))
combi1.sort(reverse=1)
combi2 = max(itertools.product(temp, repeat=len(str(n))-1))


def find_max():
    for i in combi1:
        if target >= i:
            return i
    return combi2


result = find_max()
final = ""
for i in range(len(result)):
    final += str(result[i])
print(final)
