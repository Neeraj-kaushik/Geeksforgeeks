def largest_row_and_column(n, m, li):
    largest_sum = -1
    index = -1
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += li[i][j]
        if sum > largest_sum:
            largest_sum = sum
            index = i
    for j in range(m):
        sum1 = 0
        for i in range(n):
            sum1 += li[i][j]
        if sum1 > largest_sum:
            largest_sum = sum1
            index = j
    print(largest_sum, " ", index)


t = int(input())
while t != 0:
    n = int(input())
    m = int(input())
    li = [[int(j) for j in input().split()] for i in range(n)]
    largest_row_and_column(n, m, li)
    t -= 1
