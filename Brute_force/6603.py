temp_list = []
while 1:
    temp = input()
    if temp == '0':
        break
    temp_list.append(list(map(int, temp.split())))


def solve(i, arr, result, max_len):
    if len(result) == 6:
        result.sort()
        print(' '.join(map(str, result)))
        return
    if i >= max_len:
        return

    solve(i+1, arr, [arr[i]] + result, max_len)
    solve(i+1, arr, result, max_len)


for i in temp_list:
    solve(0, i[1:], [], int(i[0]))
    print()
