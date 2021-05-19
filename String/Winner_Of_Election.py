def winner(n,li):
    max=1
    for i in range(len(li)-1):
        count=0
        for j in range(i+1,len(li)):
            if li[i]==li[j]:
                count=count+1
            if max<count:
                max=count

    small=1000
    curr=''
    if max>1:
        print(max+1)
    else:
        for k in range(len(li)):
            if len(li[k])<small:
                curr=li[k]
                small=len(li[k])
        print(curr,'1')
            




n=int(input())
li=[]
for i in range(n):
    curr=input()
    li.append(curr)
winner(n,li)