def leader_array(li):
    for i in range(len(li)):
        max=0
        for j in range(i+1,len(li)):
            if li[j]>max:
                max=li[j]
        if max<li[i]:
            print(li[i],end=' ')

            



n=int(input())
li=[int(x) for x in input().split()]
leader_array(li)