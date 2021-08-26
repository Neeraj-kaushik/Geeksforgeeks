def max_1(n, m, li):
    max1 = -1
    a = -1
    for i in range(n):
        count = 0
        for j in range(m):
            if li[i][j] == 1:
                count += 1
        if count > max1 and count > 0:
            max1 = count
            a = i
    print(a)


n = int(input())
m = int(input())
li = [[int(x) for x in input().split()] for i in range(n)]
max_1(n, m, li)
