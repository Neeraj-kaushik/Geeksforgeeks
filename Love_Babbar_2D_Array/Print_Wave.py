def print_wave(n, m, li):
    for j in range(m):
        if j % 2 == 0:
            for i in range(n):
                print(li[i][j], end=" ")
        else:
            for i in range(n-1, -1, -1):
                print(li[i][j], end=" ")


t = int(input())
while t != 0:
    n = int(input())
    m = int(input())
    li = [[int(j) for j in input().split()] for i in range(n)]
    print_wave(n, m, li)
    t -= 1
