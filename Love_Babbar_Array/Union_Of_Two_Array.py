def union_array(li, li1):
    li2 = []
    for i in li:
        if i not in li2:
            li2.append(i)
    for j in li1:
        if j not in li2:
            li2.append(j)
    print(len(li2))


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    li1 = [int(x) for x in input().split()]
    union_array(li, li1)
    t -= 1
