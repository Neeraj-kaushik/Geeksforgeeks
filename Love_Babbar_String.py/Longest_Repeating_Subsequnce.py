def longest_repeating_subsequnce(n):
    n = len(str)

    T = [[0 for i in range(n+1)]for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if((str[i-1] == str[j-1]) and (i != j)):
                T[i][j] = T[i-1][j-1] + 1

            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])

    print(T[n][n])


n = input()
longest_repeating_subsequnce(n)
