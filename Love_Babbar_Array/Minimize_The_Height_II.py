def minimize_the_height(k, li):
    li = sorted(li)
    min = li[-1]-li[0]
    small, big = 0, 0
    for i in range(1, len(li)):
        small = min(li[0]+k, li[i]-k)
        big = max(li[i-1]+k, li[-1]-k)
        ans = min(ans, big-small)
    print(ans)


k = int(input())
li = [int(x) for x in input().split()]
minimize_the_height(k, li)
