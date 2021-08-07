def rotate(arr):
    if len(arr) == 1:
        for i in arr:
            print(i)
    else:
        print(arr[-1], end=" ")
        for i in range(0, len(arr)-1):
            print(arr[i], end=" ")


n = int(input())
arr = [int(x) for x in input().split()]
rotate(arr)
