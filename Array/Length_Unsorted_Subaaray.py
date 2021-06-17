def length_subarray(li):
    li1 = sorted(li)
    count = 0
    for i in range(len(li)):
        if li[i] != li1[i]:
            count += 1
            a = i
    print(a-count, " ", a)


n = int(input())
li = [int(x) for x in input().split()]
length_subarray(li)
