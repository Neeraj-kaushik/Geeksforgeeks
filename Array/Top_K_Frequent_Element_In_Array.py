def frequent_element(li,k):
    li1=[]
    li=sorted(li)
    for i in range(len(li)-1):
        a=0
        if li[i] not in li1:
            for j in range(i+1,len(li)):
                if li[i]!=li[j]:
                    a=j-i
                    li1.append(li[i])
                    li1.append(a)
                    break             
                i=j
    print(li1)
    






li=[int(x) for x in input().split()]
k=int(input())
frequent_element(li,k)