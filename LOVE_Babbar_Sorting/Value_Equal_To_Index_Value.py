def value_equal_index_value(li):
    for i in range(len(li)):
        if li[i] == i+1:
            print(i+1, end=" ")


li = [int(x) for x in input().split()]
value_equal_index_value(li)
