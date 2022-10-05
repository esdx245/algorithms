from sys import stdin
input = stdin.readline

T = int(input())
answer = ""
result = [False, False, True] + [True, False] * 50
print(result)
print()
for number in range(3, 11, 2):
    if result[number]:
        result[number*2::number] = [False] * len(result[number*2::number])
    print(result)
    print()

# for tc in range(T):
#     N = int(input())
#     if N == 4:
#         answer += "2 2\n"
#         continue
#     harf_N = N//2
#     if not harf_N % 2:
#         harf_N += 1
#     for i in range(harf_N, N, 2):
#         if result[i] and result[N-i]:
#             answer += "{} {}".format(N - i, i) + "\n"
#             break
# print(answer, end="")
