def rotate_array(i,li):
    li2=[]
    for j in range(i,len(li)):
        li2.append(li[j])
    for j in range(0,i):
        li2.append(li[j])
    return li2



def max_sum(li,n):
    max=0
    for i in range(len(li)):
        li1=rotate_array(i,li)
        sum=0
        for k in range(len(li1)):
            sum=sum+(k*li1[k])
        if sum>max:
            max=sum
    print(max)


    



n=int(input())
li=[int(x) for x in input().split()]
max_sum(li,n)