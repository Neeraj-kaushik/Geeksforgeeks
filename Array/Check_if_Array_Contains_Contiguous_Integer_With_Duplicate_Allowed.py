def contiguous_element(li):
    li = sorted(li)
    count = 1
    for i in range(len(li)-1):
        if li[i+1]-li[i] == 1 or li[i+1] == li[i]:
            count = count+1
    if count == len(li):
        print('Yes')
    else:
        print('No')


li = [int(x) for x in input().split()]
contiguous_element(li)
