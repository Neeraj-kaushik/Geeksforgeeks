def smallest_element(k, li):
    li = sorted(li)
    print(li[k-1])


t = int(input())
while t != 0:
    k = int(input())
    li = [int(x) for x in input().split()]
    smallest_element(k, li)
    t -= 1
