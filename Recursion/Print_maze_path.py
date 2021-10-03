def pmp(sr, sc, dr, dc, ans):
    if sr == dr and sc == dc:
        print(ans)
        return
    if sr < dr:
        pmp(sr+1, sc, dr, dc, ans+'h')
    if sc < dc:
        pmp(sr, sc+1, dr, dc, ans+'v')


n = int(input())
m = int(input())
pmp(1, 1, n, m, "")
