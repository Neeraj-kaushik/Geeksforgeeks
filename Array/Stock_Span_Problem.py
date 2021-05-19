def stock_span(li):
    li1=[]
    for i in range(len(li)):
        count=1
        for j in range(0,i):
            if li[i]>li[j]:
                count=count+1
        
        li1.append(count)
    for i in range(len(li1)):
        print(li1[i],end=' ')

        



n=int(input())
li=[int(x) for x in input().split()]
stock_span(li)