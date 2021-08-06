def sort(li):
    start = 0
    end = len(li)-1
    mid = 0
    while mid <= end:
        if li[mid] == 0:
            li[start], li[mid] = li[mid], li[start]
            mid += 1
            start += 1
        elif li[mid] == 1:
            mid = mid+1
        else:
            li[mid], li[end] = li[end], li[mid]
            end -= 1
    print(li)


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    sort(li)
    t -= 1
