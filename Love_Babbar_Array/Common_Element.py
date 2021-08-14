def common_element(li, li1, li2):
    i, j, k = 0, 0, 0
    d = []
    while i < len(li) and j < len(li1) and k < len(li2):
        if li[i] < li1[j]:
            i += 1
        elif li1[j] < li[i]:
            j += 1
        else:
            if i > 0 and li[i] == li[i-1]:
                i += 1
                continue
            while k < len(li2) and li2[k] < li1[j]:
                k += 1
            if k < len(li2) and li2[k] == li1[j]:
                d.append(li2[k])
            i += 1
            j += 1
    print(d)


li = [int(x) for x in input().split()]
li1 = [int(y) for y in input().split()]
li2 = [int(z) for z in input().split()]
common_element(li, li1, li2)
