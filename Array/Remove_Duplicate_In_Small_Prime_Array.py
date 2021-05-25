def remove_duplicate(li):
    li1 = []
    for i in range(len(li)):
        if li[i] not in li1:
            li1.append(li[i])
    li = li1
    print(li)


n = int(input())
li = [int(x) for x in input().split()]
remove_duplicate(li)
