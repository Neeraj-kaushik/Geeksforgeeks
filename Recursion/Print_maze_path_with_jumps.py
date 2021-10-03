def pmpwj(sr, sc, dr, dc, ans):
    if sr == dr and sc == dc:
        print(ans, end=" ")
        return
    for i in range(1, dr-sr+1):
        l = str(i)
        pmpwj(sr+i, sc, dr, dc, ans+"h"+l)
    for i in range(1, dc-sc+1):
        l = str(i)
        pmpwj(sr, sc+i, dr, dc, ans+'v'+l)
    j = 1
    while j <= dc-sc and j <= dr-sr:
        l = str(j)
        pmpwj(sr+j, sc+j, dr, dc, ans+'d'+l)
        j += 1


n = int(input())
m = int(input())
pmpwj(1, 1, n, m, "")
