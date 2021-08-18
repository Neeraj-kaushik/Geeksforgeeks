def water_trap(li):
    r, rmax, lmax, i = 0, 0, 0, 0
    j = len(li)-1
    while i <= j:
        if li[i] <= li[j]:
            if li[i] < lmax:
                r += lmax-li[i]
            else:
                lmax = li[i]
            i += 1
        else:
            if li[j] < rmax:
                r += rmax-li[j]
            else:
                rmax = li[j]
            j -= 1
    print(r)


li = [int(x) for x in input().split()]
water_trap(li)
