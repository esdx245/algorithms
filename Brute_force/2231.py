
n = input()


def find_gen():
    if int(n) < (len(n)*1):
        print(0)
        return 0
    if int(n) < len(n)*9:
        start = 1
    else:
        start = int(n) - (len(n)*9)
    end = int(n)
    #print('start', start, 'end', end)
    for i in range(start, end):
        temp = list(map(int, str(i)))
        if sum(temp)+i == int(n):
            print(i)
            return 0
    print(0)
    return 0


find_gen()
