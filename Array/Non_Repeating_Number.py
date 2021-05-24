lst = [int(x) for x in input().strip().split(' ')]
d = {}
for j in lst:
    if j not in d:
        d[j] = 0
    d[j] += 1
p = 0
for j in lst:
    if d[j] == 1:
        print(j)
        p = 1
        break
if p == 0:
    print(-1)
