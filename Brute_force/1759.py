
l, c = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()

total = []


def check(temp):
    count = 0
    count += temp.count('a')
    count += temp.count('i')
    count += temp.count('e')
    count += temp.count('o')
    count += temp.count('u')
    return count


def solve(i, result):
    if len(result) == l:
        if 1 <= check(result) <= l-2:
            total.append(result)
        return
    if i == c:
        return

    solve(i+1, result + alpha[i])
    solve(i+1, result)


solve(0, "")
print('\n'.join(total))
