def third_largest_element(li):
    if len(li) < 3:
        print('-1')
    else:
        li = sorted(li)
        print(li[-3])


n = int(input())
li = [int(x) for x in input().split()]
third_largest_element(li)
