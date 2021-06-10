def value(li, x):
    min = 1000
    for i in range(len(li)):
        if li[i]-x == 0:
            pass
        elif li[i] < x:
            a = x-li[i]
            if a < min:
                min = a
                b = li[i]
        elif li[i] > x:
            a = li[i]-x
            if a < min:
                min = a
                b = li[i]
    li.remove(b)
    return b


def closest_element(li, k, x):
    while k != 0:
        a = value(li, x)
        print(a, end=" ")
        k = k-1


n = int(input())
li = [int(x) for x in input().split()]
k = int(input())
x = int(input())
closest_element(li, k, x)
