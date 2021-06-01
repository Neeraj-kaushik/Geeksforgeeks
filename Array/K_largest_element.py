def largest_element(li, k):
    li = sorted(li)
    i = len(li)
    j = 0
    while j != k:
        print(li[i-1], end=' ')
        i = i-1
        j = j+1


n = int(input())
k = int(input())
li = [int(x) for x in input().split()]
largest_element(li, k)
