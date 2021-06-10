def median_array(li, li1):
    i = 0
    j = 0
    li2 = []
    while i < len(li) and j < len(li1):
        if li[i] < li1[j]:
            li2.append(li[i])
            i = i+1
        if li[i] > li1[j]:
            li2.append(li1[j])
            j = j+1
    while i < len(li):
        li2.append(li[i])
        i = i+1
    while j < len(li1):
        li2.append(li1[j])
    if len(li2) % 2 == 0:
        a = len(li2)//2
        median = (li2[a]+li2[a-1])/2
        return median
    else:
        a = len(li2)//2
        return li2[a]


n = int(input())
m = int(input())
li = [int(x) for x in input().split()]
li1 = [int(x) for x in input().split()]
value = median_array(li, li1)
print(value)
