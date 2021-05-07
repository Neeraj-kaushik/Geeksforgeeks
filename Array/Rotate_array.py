def rotate_array(n,d,li):
    li2=[]
    for i in range(d,len(li)):
        li2.append(li[i])
    for i in range(0,d):
        li2.append(li[i])
    print(li2)

n=int(input())
d=int(input())
li=[int(x) for x in input().split()]
rotate_array(n,d,li)