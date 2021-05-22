def equillibrium_index(li):
    
    for i in range(len(li)-1):
        sum1=0
        sum2=0
        for j in range(0,i):
            sum1+=li[j]
        for k in range(i+1,len(li)):
            sum2+=li[k]
        if sum1==sum2:
            print(i)
    return -1



n=int(input())
li=[int(x) for x in input().split()]
equillibrium_index(li)