def facing_sun(li):
    count=1
    for i in range(1,len(li)):
        li1=[]
        for j in range(0,i):
            li1.append(li[j])
        a=max(li1)
        if a<li[i]:
            count=count+1
    print(count)
        



n=int(input())
li=[int(x) for x in input().split()]
facing_sun(li)