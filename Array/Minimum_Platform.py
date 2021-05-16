def min_platforms(li,li1,n):
    li.sort()
    li1.sort()
    i=1
    j=0
    count=1
    min=1
    while i<n and j<n:
        if li[i]<=li1[j]:
            count+=1
            i+=1
        elif li[i]>li1[j]:
            count-=1
            j=j+1
        if count>min:
            min=count

    print(min)



n=int(input())
li=[int(x) for x in input().split()]
li1=[int(x) for x in input().split()]
min_platforms(li,li1,n)