def triplet_sum(x, li):
    i = 0
    li = sorted(li)
    while i < len(li)-2:
        j = i+1
        k = len(li)-1
        while j < k:
            if li[i]+li[j]+li[k] > x:
                k = k-1
            elif li[i]+li[j]+li[k] < x:
                j += 1
            else:
                return True
        i += 1
    return False


x = int(input())
li = [int(x) for x in input().split()]
if(triplet_sum(x, li)):
    print("1")
else:
    print("0")
