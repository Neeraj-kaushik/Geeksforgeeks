def sorted1(n, li):
    for i in range(0, n):
        for j in range(0, n):
            print(li[i][j])


n = int(input())
li = [[int(j) for j in input().split()] for i in range(n)]
sorted1(n, li)
