def count_triplet(li):
    count=0
    for i in range(len(li)-1):
        sum=li[i]
        for j in range(i+1,len(li)):
            sum=sum+li[j]
            for k in range(len(li)):
                if sum==li[k]:
                    count=count+1
    if count==0:
        print('0')
    else: 
        print(count+1)


n=int(input())
li=[int(x) for x in input().split()]
count_triplet(li)