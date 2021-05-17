def common_element(n1,n2,n3,li,li1,li2):
    for i in range(len(li)):
        for j in range(len(li1)):
            for k in range(len(li2)):
                if li[i]==li1[j]==li2[k]:
                    print(li[i],end=' ')
                    




n1=int(input())
n2=int(input())
n3=int(input())
li=[int(x) for x in input().split()]
li1=[int(y) for y in input().split()]
li2=[int(z) for z in input().split()]
common_element(n1,n2,n3,li,li1,li2)