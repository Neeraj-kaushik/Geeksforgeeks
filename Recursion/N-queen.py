def queensafe(li, row, col):
    i = row-1
    j = col
    while i >= 0:
        if li[i][j] == 1:
            return False
        i -= 1
    k = row-1
    l = col-1
    while k >= 0 and l >= 0:
        if li[k][l] == 1:
            return False
        k -= 1
        l -= 1
    m = row-1
    n = col+1
    while m >= 0 and n < len(li):
        if li[m][n] == 1:
            return False
        m -= 1
        n += 1
    return True


def queen(li, ans, row):
    for col in range(len(li)):
        if row == len(li):
            print(ans)
            return

        if queensafe(li, row, col) == True:
            li[row][col] = 1
            queen(li, ans+str(row)+"-"+str(col)+",", row+1)
            li[row][col] = 0


n = int(input())
li = [[0 for j in range(n)] for i in range(n)]
queen(li, "", 0)
