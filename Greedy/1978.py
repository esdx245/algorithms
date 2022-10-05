from tkinter.tix import Tree


n = int(input())
lista = map(int, input().split())
decimal = 0
for i in lista:
    error = False
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error = Tree
                break
        if error == 0:
            decimal += 1
print(decimal)
