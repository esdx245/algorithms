a, b, c, m = map(int, input().split())
piro = 0


def solve(time, piro, result):
    if time == 24:
        print(result)
        return
    if piro < 0:
        piro = 0
    if piro+a <= m:
        solve(time+1, piro+a, result+b)
    else:
        solve(time+1, piro-c, result)


solve(0, 0, 0)
