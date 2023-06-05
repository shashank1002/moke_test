n = input()
for i in list(n):
    if n.count(i) == 1:
        print(n.index(i))
        break
    elif n[-1] == i:
        print(-1)