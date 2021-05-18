def find_two_element(n,li):
    j=1
    for i in range(len(li)-1):
        for k in range(i+1,len(li)):
            if li[i]==li[k]:
                d=li[k]
            if j not in li:
                c=j
            else:
                j=j+1
    print(d,' ',c)



n=int(input())
li=[int(x) for x in input().split()]
find_two_element(n,li)