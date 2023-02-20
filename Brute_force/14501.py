n = int(input())
day_cost = [list(map(int, input().split())) for _ in range(n)]
max_cost = 0


def solve(i, cost_sum):
    global max_cost
    if i >= n:
        if i == n:
            temp = sum(cost_sum)
        else:
            temp = sum(cost_sum[:-1])
        if temp > max_cost:
            max_cost = temp

        return
    solve(i+1, cost_sum)
    solve(i+day_cost[i][0], cost_sum+[day_cost[i][1]])


solve(0, [])
print(max_cost)
