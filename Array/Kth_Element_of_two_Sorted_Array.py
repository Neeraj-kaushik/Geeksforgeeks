def kth_element(li, li1, k):
    li2 = []
    i = 0
    j = 0
    while i < len(li) and j < len(li1):
        if li[i] < li1[j]:
            li2.append(li[i])
            i = i+1
        else:
            li2.append(li1[j])
            j = j+1
    while i < len(li):
        li2.append(li[i])
        i = i+1
    while j < len(li1):
        li2.append(li1[j])
        j = j+1
    i = 0
    while i <= len(li2):
        if i == k:
            print(li2[i-1])
            break
        i = i+1


li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
k = int(input())
kth_element(li, li1, k)
