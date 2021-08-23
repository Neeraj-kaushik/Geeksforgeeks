def spiral(n, m, li):
    i, j, k, l = 0, 0, n-1, m-1
    while i <= k and j <= l:
        for x in range(j, k+1):
            print(li[i][x], end=" ")
        i += 1
        for x in range(i, l+1):
            print(li[x][k], end=" ")
        k -= 1
        if i <= l:
            for x in range(k, j-1, -1):
                print(li[l][x], end=" ")
            l -= 1
        if j <= k:
            for x in range(l, i-1, -1):
                print(li[x][j], end=" ")
            j += 1


n = int(input())
m = int(input())
li = [[int(j) for j in input().split()] for i in range(n)]
spiral(n, m, li)
