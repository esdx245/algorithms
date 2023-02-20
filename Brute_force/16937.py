#import sys
#input = sys.stdin.readline
h, w = map(int, input().split())
n = int(input())
sticker = [list(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n):
    r1 = sticker[i][0]
    c1 = sticker[i][1]
    for j in range(i+1, n):
        r2 = sticker[j][0]
        c2 = sticker[j][1]

        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        elif (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        elif (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)
        elif (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)
print(result)
