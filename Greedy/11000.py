import sys
import heapq
input = sys.stdin.readline
case = int(input())
q = []

for i in range(case):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

classs = []
heapq.heappush(classs, q[0][1])

for i in range(1, case):
    if q[i][0] < classs[0]:
        heapq.heappush(classs, q[i][1])
    else:
        heapq.heappop(classs)
        heapq.heappush(classs, q[i][1])
print(len(classs))
