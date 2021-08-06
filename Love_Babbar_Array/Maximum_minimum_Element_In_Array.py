def max_min(arr):
    max = 0
    min = 1000000
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    print(max, min)


t = int(input())
while t != 0:
    arr = [int(x) for x in input().split()]
    max_min(arr)
    t = t-1
