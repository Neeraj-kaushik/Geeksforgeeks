def insert(li):
    d=[]
    for i in range(0,len(li)-2,2):
        if li[i]=='a':
            d.append(li[i+1])
    return d

def increase(a,li):
    if li[-3]=='i':
        a=sorted(a)
    return a

def decrease(a,li):
    if li[-3]=='d':
        for i in range(len(a)):
            if a[i]<a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    return a

def search(b,li):
    s=li[-1]
    for i in range(len(b)):
        if b[i]==s:
            print(i)
            break
    



n=int(input())
li=input().split()
for i in range(len(li)):
    if li[i]=='a':
        a=insert(li)

    elif li[i]=='i':
        b=increase(a,li)
    
    elif li[i]=='d':
        b=decrease(a,li) 

    elif li[i]=='s':
        search(b,li)   