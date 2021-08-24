def search(n, m, x, li):
    value = False
    for j in range(0, 1):
        for i in range(n):
            if li[i][j] < x:
                continue
            elif li[i][j] == x:
                value = True
            else:
                a = i-1
                break
    for i in range(a, a+1):
        for j in range(m):
            if li[i][j] == x:
                value = True
    if value == True:
        print("true")
    else:
        print("false")


n = int(input())
m = int(input())
x = int(input())
li = [[int(j) for j in input().split()]for i in range(n)]
search(n, m, x, li)
