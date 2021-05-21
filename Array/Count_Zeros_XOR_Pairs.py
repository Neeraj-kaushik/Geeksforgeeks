def count_xor(li):
    count=0
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]^li[j]==0:
                count=count+1
    print(count)



li=[int(x) for x in input().split()]
count_xor(li)