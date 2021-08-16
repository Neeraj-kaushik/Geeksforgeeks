def longest_sequence(li):
    li = sorted(li)
    print(li)
    k, i, count, max1 = 1, 0, 1, 0
    if len(li) == 1:
        print("1")
    while i <= len(li) and k <= len(li)-1:
        if li[k]-li[i] == 1:
            count += 1
            if count > max1:
                max1 = count
            k += 1
            i += 1
        elif li[k]-li[i] == 0:
            k += 1
            i += 1
        else:
            k += 1
            count = 1
            i += 1
    max1 = max(max1, count)
    print(max1)


li = [int(x) for x in input().split()]
longest_sequence(li)
