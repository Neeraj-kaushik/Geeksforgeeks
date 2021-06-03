def not_subset(li):
    m = 1
    for i in range(len(li)):
        if li[i] > m:
            print(m)
        else:
            m += li[i]
    print(m)


n = int(input())
li = [int(x) for x in input().split()]
not_subset(li)
