def counting_element(li,li1):
    li2=[]
    for i in range(len(li)):
        count=0
        max=0
        for j in range(len(li1)):
            if li1[j]<=li[i]:
                count=count+1
        li2.append(count)
    for i in range(len(li2)):
        print(li2[i],end=' ')
                


n=int(input())
m=int(input())
li=[int(x) for x in input().split()]
li1=[int(x) for x in input().split()]
counting_element(li,li1)