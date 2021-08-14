def rotate(li, s, e):
    li.insert(s, li.pop(e))


def rearrange(li):
    i, j, k = 0, 0, 0
    while i < len(li) and j < len(li) and k < len(li):
        if k % 2 == 0:
            if li[k] >= 0:
                i = k
                j = k
                while i < len(li) and li[i] >= 0:
                    i += 1
                if i >= len(li):
                    break
                rotate(li, j, i)
        else:
            if li[k] < 0:
                i = k
                j = k
                while j < len(li) and li[j] < 0:
                    j += 1
                if j >= len(li):
                    break
                rotate(li, i, j)
        k += 1
    print(li)


li = [int(x) for x in input().split()]
rearrange(li)
