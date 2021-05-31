def merge_array(li, li1):
    for i in range(len(li)):
        for j in range(len(li1)):
            if li[i] > li1[j]:
                li[i], li1[j] = li1[j], li[i]
    li1 = sorted(li1)
    for i in range(len(li)):
        print(li[i], end=' ')
    for j in range(len(li1)):
        print(li1[j], end=' ')


n = int(input())
m = int(input())
li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
merge_array(li, li1)
