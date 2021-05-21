def subarray_0_1(li):
    count=0
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            count0=0
            count1=0
            for k in range(i,j):
                if li[k]==1:
                    count1+=1
                if li[k]==0:
                    count0+=1
            if count1==count0:
                count+=1
    
    print(count+1)


n=int(input())
li=[int(x) for x in input().split()]
subarray_0_1(li)