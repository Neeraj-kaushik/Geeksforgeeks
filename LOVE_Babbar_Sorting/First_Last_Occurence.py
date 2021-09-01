def f_l_o(n, x, li):
    s, res1, res2 = 0, 0, 0
    e = len(li)-1
    a = 0
    b = len(li)-1
    while s <= e:
        m = int(s+(e-s)/2)
        if li[m] == x:
            res1 = m
            e = m-1
        elif li[m] > x:
            e = m-1
        else:
            s = m+1
    while a <= b:
        mid = int(a+(b-a)/2)
        if li[mid] == x:
            res2 = mid
            a = mid+1
        elif li[mid] > x:
            b = mid-1
        else:
            a = mid+1
    print(res1, res2)


n = int(input())
x = int(input())
li = [int(x) for x in input().split()]
f_l_o(n, x, li)
