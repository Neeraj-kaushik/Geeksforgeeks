def merge_array(li, li1):
    i, j = 0, 0
    k = len(li)-1
    while i <= k and j < len(li1):
        if li[i] < li1[j]:
            i += 1
            continue
        else:
            li[k], li1[j] = li1[j], li[k]
            j += 1
            k -= 1
    li.sort()
    li1.sort()


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    li1 = [int(x) for x in input().split()]
    ans = merge_array(li, li1)
    for i in range(len(li)):
        print(li[i], end=" ")
    for j in range(len(li1)):
        print(li1[j], end=" ")
    t -= 1
