n=int(input())
st=['!','#','$','%','&','*','@','^','~']
li1=input().split()
li2=input().split()
d=[]
for i in st:
    if i in li1:
        d.append(i)
for i in d:
    print(i,end=' ')
print()
for i in d:
    print(i,end=' ')
print()