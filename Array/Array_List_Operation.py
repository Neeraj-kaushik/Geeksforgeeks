def frequency(li):
    li1=[]
    for k in range(0,len(li)-1,2):
        if li[k]=='i':
            li1.append(li[k+1])
        else:
            count=0
            for i in range(len(li1)):
                if li[k+1]==li1[i]:
                    count=count+1
            if count==0:
                print('0')
            else:
                print(count)



n=int(input())
li=input().split()
frequency(li)