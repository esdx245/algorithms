
t = input()
name_list = list(set(t))
name_list.sort()
name_count = []
for i in name_list:
    name_count.append(t.count(str(i)))

n = int(input())
temp = [[0 for _ in range(len(name_list)+1)] for _ in range(n)]

book = []
for i in range(n):
    p, name = input().split()
    name = list(name)
    name.sort()
    book += [[int(p), name]]
#book.sort(key = lambda x: [x][0])


for i in range(n):
    book_name = book[i][1]
    temp[i][0] = book[i][0]
    for j in range(len(name_list)):
        if name_list[j] in book_name:
            temp[i][j+1] += book_name.count(name_list[j])


min_price = 999999999


def solve(i, t_list, t_price):
    global min_price
    count = 0
    for k in range(len(t_list)):
        if t_list[k] >= name_count[k]:
            count += 1
    if count == len(t_list):
        min_price = min(min_price, t_price)
        return
    if i >= n:
        return

    solve(i+1, t_list, t_price)
    new_list = [0 for _ in range(len(name_list))]
    for j in range(len(t_list)):
        new_list[j] = t_list[j] + temp[i][j+1]
    solve(i+1, new_list, t_price+temp[i][0])


solve(0, [0 for _ in range(len(name_list))], 0)
if min_price != 999999999:
    print(min_price)
else:
    print(-1)
