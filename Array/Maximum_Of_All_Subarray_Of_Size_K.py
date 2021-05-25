def max_of_subarray(n, k, li):
    li1 = []
    for i in range(len(li)-k+1):
        max = 0
        for j in range(i, i+k):
            if li[j] > max:
                max = li[j]
        print(max, end=" ")


n = int(input())
k = int(input())
li = [int(x) for x in input().split()]
max_of_subarray(n, k, li)
