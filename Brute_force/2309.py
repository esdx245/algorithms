import itertools


def sol():
    height = []
    for _ in range(0, 9):
        height.append(int(input()))
    height.sort()
    temp = list(itertools.combinations(height, 7))
    for i in temp:
        if sum(i) == 100:
            for j in i:
                print(j)
            return 0


sol()
