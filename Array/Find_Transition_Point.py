n=int(input())
li=[int(x) for x in input().split()]
if li[0]==1:
    print('0')
elif li[-1]==0:
    print('-1')
    
for i in range(len(li)-1):
    if li[i]==1:
        print(i)