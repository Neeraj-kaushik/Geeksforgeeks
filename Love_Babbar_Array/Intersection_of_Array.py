def intersection(li, li1):
    li2 = []
    for i in li:
        if i in li1:
            li2.append(i)
    print(li2)


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    li1 = [int(x) for x in input().split()]
    intersection(li, li1)
    t -= 1
