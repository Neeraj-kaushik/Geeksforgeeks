def insertion_sort(n,li):
    for i in range(1,len(li)):
        curr_element=li[i]
        pos=i
        while curr_element<li[pos-1] and pos>0:
            li[pos]=li[pos-1]
            pos=pos-1
        li[pos]=curr_element
    print(li)

n=int(input())
li=[int(x) for x in input().split()]
insertion_sort(n,li)