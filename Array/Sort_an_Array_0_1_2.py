def sort_array(li):
    start=0
    end=n-1
    i=0
    while i<=end:
        if li[i]==0:
            temp=li[i]
            li[i]=li[start]
            li[start]=temp
            i=i+1
            start+=1
        elif li[i]==2:
            temp=li[i]
            li[i]=li[end]
            li[end]=temp
            i=i+1
            end-=1
        else:
            i=i+1
    print(li)

n=int(input())
li=[int(x) for x in input().split()]
sort_array(li)