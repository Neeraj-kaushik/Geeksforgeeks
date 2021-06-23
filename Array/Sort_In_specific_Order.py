def sort_specific(li):
    li1 = []
    li2 = []
    for i in range(len(li)):
        if li[i] % 2 == 0:
            li1.append(li[i])
        else:
            li2.append(li[i])
    li1 = sorted(li1)
    li2 = sorted(li2)
    li2 = li2[::-1]
    li3 = li2+li1
    print(li3)


n = int(input())
li = [int(x) for x in input().split()]
sort_specific(li)
