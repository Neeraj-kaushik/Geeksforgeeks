def row_wise_sum(n, m, li):
    for row in li:
        sum = 0
        for ele in row:
            sum += ele
        print(sum, end=" ")


t = int(input())
while t != 0:
    n = int(input())
    m = int(input())
    li = [(int(j) for j in input().split()) for i in range(n)]
    row_wise_sum(n, m, li)
    t -= 1
