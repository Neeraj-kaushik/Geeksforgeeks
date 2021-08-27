def Specific_Pair(n, m, li):
    max1 = -1
    for i in range(n-1):
        for j in range(m-1):
            for k in range(i+1, n):
                for l in range(j+1, m):
                    if max1 < li[k][l]-li[i][j]:
                        max1 = li[k][l]-li[i][j]
    print(max1)


n = int(input())
m = int(input())
li = [[int(j) for j in input().split()] for i in range(n)]
Specific_Pair(n, m, li)
