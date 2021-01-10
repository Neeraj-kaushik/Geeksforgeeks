def gmp(sr, sc, dr, dc):
    if sr == dr and sc == dc:
        li1 = []
        li1.append("")
        return li1
    li2 = []
    i = 1
    while i <= dc-sc:
        path2 = gmp(sr, sc+i, dr, dc)
        x = str(i)
        for ele in path2:
            li2.append('h'+x+ele)
        i += 1
    z = 1
    while z <= dr-sr:
        path1 = gmp(sr+1, sc, dr, dc)
        k = str(z)
        for ele in path1:
            li2.append('v'+k+ele)
        z += 1

    j = 1
    while j <= dr-sr and j <= dc-sc:
        path3 = gmp(sr+j, sc+j, dr, dc)
        l = str(j)
        for ele in path3:
            li2.append('d'+l + ele)
        j += 1
    return li2


n = int(input())
m = int(input())
li = gmp(1, 1, n, m)
print(li)
