import itertools

n = int(input())
possible = list(itertools.permutations(range(1, 10), 3))


def check(ori, temp):
    strike = 0
    ball = 0
    if str(temp[0]) in ori:
        if str(temp[0]) == ori[0]:
            strike += 1
        else:
            ball += 1
    if str(temp[1]) in ori:
        if str(temp[1]) == ori[1]:
            strike += 1
        else:
            ball += 1
    if str(temp[2]) in ori:
        if str(temp[2]) == ori[2]:
            strike += 1
        else:
            ball += 1

    return [strike, ball]


def solve(i, possible_list, result_list):
    if i >= n:
        print(len(possible_list))
        return

    tar, strike, ball = map(int, input().split())
    for j in range(len(possible_list)):
        if check(str(tar), possible_list[j]) == [strike, ball]:
            result_list.append(possible_list[j])
    #print('i = {}, result_list = {}'.format(i, result_list))
    solve(i+1, result_list, [])


solve(0, possible, [])
