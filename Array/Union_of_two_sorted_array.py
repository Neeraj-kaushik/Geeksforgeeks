def union(n,li,m,li2):
    li3=[]
    for i in range(len(li)):
        for j in range(len(li2)):
            if li[i]==li[j]:
                li3.append(li[i])
            elif li[i]!=li[j] or li[j]!=li[i]:
                li3.append(li[i])
                li3.append(li[j])
    print(li3)



n=int(input())
li=[int(x) for x in input().split()]
m=int(input())
li2=[int(y) for y in input().split()]
union(n,li,m,li2)