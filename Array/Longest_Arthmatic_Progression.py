def longest_ap(a, n):
    if(n < 2):
        return n
    a.sort()
    dp = [[-1000]*n for i in range(n)]

    for i in range(n):
        dp[i][n-1] = 2
    maxlength = 2
    for j in range(n-2, 0, -1):
        i = j-1
        k = j+1

        while(i >= 0 and k < n):
            if(a[i] + a[k] == 2*a[j]):
                dp[i][j] = dp[j][k]+1
                if(maxlength < dp[i][j]):
                    maxlength = dp[i][j]
                i -= 1
                k += 1
            elif(a[i]+a[k] < 2*a[j]):
                k += 1
            else:
                dp[i][j] = 2
                i -= 1
        while(i >= 0):
            dp[i][j] = 2
            i -= 1

    return maxlength


t = int(input())
for testcase in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(longest_ap(arr, n))
