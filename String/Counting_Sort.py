def sort(str):
    li=[]
    for i in range(len(str)):
        li.append(str[i])
        li.sort()
    for i in range(len(li)):
        print(li[i],end='')
        
        
    

n=int(input())
str=input()
sort(str)