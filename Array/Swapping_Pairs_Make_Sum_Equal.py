def sum_of_both(a, b):
    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        sum1 = sum1+a[i]
    for i in range(len(b)):
        sum2 = sum2+b[i]
    if sum1 == sum2:
        return 1
    else:
        return 0


def swapping_pair(li, li1):
    count = 0
    a = li
    b = li1
    for i in range(len(a)):
        for j in range(len(b)):
            a = li
            b = li1
            print(li)
            print(li1)
            a[i], b[j] = b[j], a[i]
            print(a)
            print(b)
            value = sum_of_both(a, b)
            print(value)
            if value == 1:
                count += 1
    print(count)


n = int(input())
m = int(input())
li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
swapping_pair(li, li1)
