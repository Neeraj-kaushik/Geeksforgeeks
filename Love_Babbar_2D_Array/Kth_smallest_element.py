def kth_smallest_element(n, m, li, k):
    sval = li[0][0]
    enval = li[n-1][m-1]
    while sval <= enval:
        ans = 0
        mval = (sval+enval)//2
        for i in range(n):
            l = 0
            h = m-1
            while l <= h:
                mid = int(l+(h-l)/2)
                if li[i][mid] <= mval:
                    l = mid+1
                else:
                    h = mid-1
            ans += l
        if ans < k:
            sval = mval+1
        else:
            enval = mval-1
    print(sval)


n = int(input())
m = int(input())
li = [[int(j) for j in input().split()] for i in range(n)]
k = int(input())
kth_smallest_element(n, m, li, k)
