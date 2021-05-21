def partioning(li,a,b):
    li1=[]
    li2=[]
    li3=[]
    for i in range(len(li)):
        if li[i]<=a:
            li1.append(li[i])
        if li[i]>a and li[i]<b:
            li2.append(li[i])
        if li[i]>=b:
            li3.append(li[i])
    if len(li)==len(li1)+len(li2)+len(li3):
        print('1')
    else:
        print('0')




n=int(input())
li=[int(x) for x in input().split()]
a=int(input())
b=int(input())
partioning(li,a,b)
