def merge(li, s, mid, e):
    n1 = mid-s+1
    n2 = e-mid
    li1 = [0]*n1
    li2 = [0]*n2
    for i in range(0, n1):
        li1[i] = li[s+i]
    for j in range(0, n2):
        li2[j] = li[mid+1+j]
    i, j, k = 0, 0, 0
    while i <= n1 and j <= n2:
        if li1[i] < li2[j]:
            li[k] = li1[i]
            i += 1
        else:
            li[k] = li2[j]
            j += 1
        k += 1
    while i <= n1:
        li[k] = li1[i]
        i += 1
        k += 1
    while j <= n2:
        li[k] = li2[j]
        j += 1
        k += 1


def mergesort(li, s, e):
    count = 0
    if s < e:
        mid = e-s//2
        count += mergesort(li, s, mid)
        count += mergesort(li, mid+1, e)
        count += merge(li, s, mid, e)
    return count


def count_inversion(li):
    ans = mergesort(li, s=0, e=len(li)-1)
    print(ans)


t = int(input())
while t != 0:
    li = [int(x) for x in input().split()]
    count_inversion(li)
    t -= 1
