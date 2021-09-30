def maze(sr, sc, dr, dc):
    if sc == dc and sr == dr:
        li1 = []
        li1.append("")
        return li1

    hpath, vpath, li2 = [], [], []
    if sr < dr:
        hpath = maze(sr+1, sc, dr, dc)
    if sc < dc:
        vpath = maze(sr, sc+1, dr, dc)
    for ele in hpath:
        li2.append('h'+ele)
    for ele in vpath:
        li2.append('v'+ele)
    return li2


n = int(input())
m = int(input())
li = maze(1, 1, n, m)
print(li)
