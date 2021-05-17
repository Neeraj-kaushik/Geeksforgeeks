def repeating_element(li):
    a=0
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i]==li[j]:
                a=i+1
                break
    if a==0:
        print('-1')
    else:
        print(a)

    

n=int(input())
li=[int(x) for x in input().split()]
repeating_element(li)
