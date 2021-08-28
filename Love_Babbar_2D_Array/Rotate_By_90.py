def rotate(n, m, li):
    for j in range(m):
        for i in range(n-1, -1, -1):
            print(li[i][j], end=" ")
        print()


n = int(input())
m = int(input())
li = [[int(j) for j in input().split()] for i in range(n)]
rotate(n, m, li)
