def median(n, m, li):
    val1 = 0
    n = n*m
    val2 = 2000
    while val1 <= val2:
        ans = 0
        midvalue = (val1+val2)//2
        for i in range(n):
            l = 0
            h = m-1
            while l <= h:
                m = int(l+(h-l)/2)
                if li[i][m] <= midvalue:
                    l = m+1
                else:
                    h = m-1
            ans += l
        if ans <= n//2:
            val1 = midvalue+1
        else:
            val2 = midvalue-1
    print(val1)


n = int(input())
m = int(input())
li = [[int(x) for x in input().split()] for i in range(n)]
median(n, m, li)
