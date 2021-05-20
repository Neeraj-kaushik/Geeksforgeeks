def number_formation(li):
    sum=0
    for i in li:
        k=i
        while k!=0:
            mod=k%10
            sum=sum+mod
            k=k//10
    if sum%3==0:
        print('1')
    else:
        print('0')


n=int(input())
li=[int(x) for x in input().split()]
number_formation(li)