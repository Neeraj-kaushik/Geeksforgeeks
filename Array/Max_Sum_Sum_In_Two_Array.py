def max_sum_path(m,n,li,li1):
    i=j=sum1=sum2=temp=tepm1=0
    for i in range(len(li)):
        for j in range(len(li1)):
            if li[i]==li1[j]:
                a=i
                b=j
                for i in range(0,a):
                    sum1=sum1+li[i]
            
                for j in range(0,b):
                    sum2=sum2+li1[j]
            
                if sum1>sum2:
                    temp=temp1=sum1
                    for i in range(a,len(li)):
                        temp=temp+li[i]
                    for j in range(b,len(li1)):
                        temp1=temp1+li1[j]
                    if temp >temp1:
                        print(temp)
                    else:
                        print(temp1)
                else:
                    temp=temp1=sum2
                    for i in range(a,len(li)):
                        temp=temp+li[i]
                    
                    for j in range(b,len(li1)):
                        temp1=temp1+li1[j]
                    
                    if temp >temp1:
                        print(temp)
                    else:
                        print(temp1)
    




    



m=int(input())
n=int(input())
li=[int(x) for x in input().split()]
li1=[int(y) for y in input().split()]
max_sum_path(m,n,li,li1)