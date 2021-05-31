def union(n, li, m, li2):
    li3 = []
    for i in range(len(li)):
        if li[i] not in li3:
            li3.append(li[i])
    for i in range(len(li2)):
        if li2[i] not in li3:
            li3.append(li2[i])
    li3 = sorted(li3)
    print(li3)


n = int(input())
li = [int(x) for x in input().split()]
m = int(input())
li2 = [int(y) for y in input().split()]
union(n, li, m, li2)
