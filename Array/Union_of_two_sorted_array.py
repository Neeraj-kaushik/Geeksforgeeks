def union(n,li,m,li2):
    li3=[]
    i=0
    j=0
    while i<n and j <m:
        if li[i]<li2[j]:
            li3.append(li[i])
            i=i+1
        elif li2[j]<li[i]:
            li3.append(li2[j])
            j=j+1
        else:
            li3.append(li2[j])
            i=i+1
            j=j+1
    while i <n:
        li3.append(li[i])
        i=i+1
    while j<m:
        li3.append(li2[j])
        j=j+1
    print(li3)



n=int(input())
li=[int(x) for x in input().split()]
m=int(input())
li2=[int(y) for y in input().split()]
union(n,li,m,li2)