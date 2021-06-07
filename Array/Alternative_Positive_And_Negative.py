def arrange(n, li):
    li1 = []
    li2 = []
    li3 = []
    for i in range(len(li)):
        if li[i] < 0:
            li2.append(li[i])
        else:
            li1.append(li[i])
    j = 0
    k = 0
    l = 0
    while l <= n+1:
        if l % 2 == 0 and j < len(li1):
            li3.append(li1[j])
            j = j+1
        elif l % 2 != 0 and k < len(li2):
            li3.append(li2[k])
            k = k+1
        elif k == len(li2) and j < len(li1):
            break
        elif j == len(li1) and k < len(li2):
            break
        l += 1
    while l <= n+1:
        if j < len(li1):
            li3.appen(li1[j])
            j = j+1
        elif k < len(li2):
            li3.append(li2[k])
            k = k+1
        l = l+1
    print(li3)


n = int(input())
li = [int(x) for x in input().split()]
arrange(n, li)
