def sum_array(li):
    if len(li) == 0:
        return 0
    return li[0]+sum_array(li[1:])


li = [int(x) for x in input().split()]
print(sum_array(li))
